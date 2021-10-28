#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
使用DefautSelector改造, 在支持epoll的平台上会使用epoll实现
"""

from collections import deque
from select import select
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE


# This class represents a generic yield event in the scheduler
class YieldEvent:

    def __init__(self):
        pass

    def handle_yield(self, sched, task):
        pass

    def handle_resume(self, sched, task):
        pass


# Task Scheduler
class Scheduler:
    def __init__(self):
        self._numtasks = 0  # Total num of tasks
        self._ready = deque()  # Tasks ready to run
        self._selector = DefaultSelector()  # Higher level i/o multiplexing library

    # Poll for I/O events and restart waiting tasks
    def _iopoll(self):
        ready_list = self._selector.select()
        for ready in ready_list:
            key = ready[0]
            evt, task = key.data
            self._selector.unregister(key.fileobj)
            evt.handle_resume(self, task)

    def new(self, task):
        """
        Add a newly started task to the scheduler
        """
        self._ready.append((task, None))
        self._numtasks += 1

    def add_ready(self, task, msg=None):
        """
        Append an already started task to the ready queue.
        msg is what to send into the task when it resumes.
        """
        self._ready.append((task, msg))

    # Add a task to the reading set
    def _read_wait(self, fileno, evt, task):
        try:
            self._selector.get_key(fileno)
        except KeyError:
            self._selector.register(fileno, EVENT_READ, data=(evt, task))

    # Add a task to the write set
    def _write_wait(self, fileno, evt, task):
        try:
            self._selector.get_key(fileno)
        except KeyError:
            self._selector.register(fileno, EVENT_WRITE, data=(evt, task))

    def run(self):
        """
        Run the task scheduler until there are no tasks
        """
        while self._numtasks:
            if not self._ready:
                self._iopoll()
            task, msg = self._ready.popleft()
            try:
                # Run the coroutine to the next yield
                r = task.send(msg)
                if isinstance(r, YieldEvent):
                    r.handle_yield(self, task)
                else:
                    raise RuntimeError('unrecognized yield event')
            except StopIteration:
                self._numtasks -= 1


# Example implementation of coroutine-based socket I/O
class ReadSocket(YieldEvent):
    def __init__(self, sock, nbytes):
        self.sock = sock
        self.nbytes = nbytes

    def handle_yield(self, sched, task):
        sched._read_wait(self.sock.fileno(), self, task)

    def handle_resume(self, sched, task):
        data = self.sock.recv(self.nbytes)
        sched.add_ready(task, data)


class WriteSocket(YieldEvent):
    def __init__(self, sock, data):
        self.sock = sock
        self.data = data

    def handle_yield(self, sched, task):
        sched._write_wait(self.sock.fileno(), self, task)

    def handle_resume(self, sched, task):
        nsent = self.sock.send(self.data)
        sched.add_ready(task, nsent)


class AcceptSocket(YieldEvent):
    def __init__(self, sock):
        self.sock = sock

    def handle_yield(self, sched, task):
        sched._read_wait(self.sock.fileno(), self, task)

    def handle_resume(self, sched, task):
        r = self.sock.accept()
        sched.add_ready(task, r)


# Wrapper around a socket object for use with yield
class Socket(object):
    def __init__(self, sock):
        self._sock = sock

    def recv(self, maxbytes):
        return ReadSocket(self._sock, maxbytes)

    def send(self, data):
        return WriteSocket(self._sock, data)

    def accept(self):
        return AcceptSocket(self._sock)

    def __getattr__(self, name):
        return getattr(self._sock, name)


if __name__ == '__main__':
    from socket import socket, AF_INET, SOCK_STREAM
    import time

    # Example of a function involving generators.  This should
    # be called using line = yield from readline(sock)
    def readline(sock):
        chars = []
        while True:
            c = yield sock.recv(1)
            if not c:
                break
            chars.append(c)
            if c == b'\n':
                break
        return b''.join(chars)

    # Echo server using generators
    class EchoServer:
        def __init__(self, addr, sched):
            self.sched = sched
            sched.new(self.server_loop(addr))

        def server_loop(self, addr):
            s = Socket(socket(AF_INET, SOCK_STREAM))

            s.bind(addr)
            s.listen(5)
            while True:
                c, a = yield s.accept()
                print('Got connection from ', a)
                self.sched.new(self.client_handler(Socket(c)))

        def client_handler(self, client):
            while True:
                line = yield from readline(client)
                print(line)
                if not line:
                    break
                line = b'GOT:' + line
                while line:
                    nsent = yield client.send(line)
                    line = line[nsent:]
            client.close()
            print('Client closed')


    scheduler = Scheduler()
    EchoServer(('', 16000), scheduler)
    scheduler.run()

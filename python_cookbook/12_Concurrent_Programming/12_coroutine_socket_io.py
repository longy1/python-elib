#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
流程
实例化Scheduler
    维护任务数, 就绪队列, 等待读列表, 等待写列表
一个本地地址和一个调度器实例化EchoServer
    EchoServer维护调度器引用
    EchoServer把server_loop(addr)装入调度器就绪队列
    server_loop开始执行会阻塞在yield等待socket accept建立连接
第一次调度器run方法, 对任务数死循环
    task, msg = self._ready.popleft()
    此时task = server_loop(addr), msg = None
    r = task.send(msg), 即用None启动server_loop方法
第一次server_loop
    实例化包装版Socket, bind, listen
    直到底层accept请求进入, yield AcceptSocket对象, 这是一个YieldEvent
yield返回到run方法
    判断r是否为YieldEvent, 若是, 则调用r自身的handle_yield(self, task)方法处理task
    传入了self, 即告诉了YieldEvent调度器的引用
AcceptSocket.handle_yield接收到sched与task
    此时task仍然是server_loop
    调用sched._read_wait(fileno, self, task)进行读等待
    _read_wait会将fileno添加到_read_waiting中, 值为evt, task
此时完成了Accept的初始化, 并且开始等待socket读取
第二次run, 就绪队列为空, 调用_iopoll()
第一次_iopoll(), 读等待列表存在socket
    通过select系统调用, 阻塞等待到新的读就绪, 写就绪, 异常就绪fileno集合
    对于读就绪集合:
        获取其evt, task
        调用evt的回调handle_resume, 传入sched与task
    对于写就绪的集合:
        读取其evt, task
        调用evt的回调handle_resume, 传入sched与task
第一次读回调AcceptSocket.handle_resume
    此时真正处理accept请求
    socket.accept()获取了socket与addr对象
    将server_loop, (socket, addr)加入就绪队列
第三次run, 就绪队列存在server_loop, 出队并send((socekt, addr))
回到server_loop
    c, a接受了调度器send的socket, addr
    向调度器加入client_handler(Socket(c))
    server_loop继续yield出一个AcceptSocekt事件给调度器, 循环之前的读取等待
在新一轮run时, 开始执行client_handler(Socket(c))
    此时, 该Socket对象是一个连接socket, 称为client
    使用readline(client)尝试读取socket
    获得line之后, 使用client.send(line), 调用Socket.send()
获得line使用了Socket的recv(maxbytes)方法, 该方法接受单次读取最大长度作为参数, 并用其实例化一个ReadSocket事件
Socket.send(self, data)用data实例化一个等待Write事件, 被run中的r获取后, 通过handle_yield, 将socket的fileno加入等待写列表
经过select后, 等待写列表会就绪, 则该data实际被发出

特征
除了就绪队列为空时需要_iopoll进而select进行轮询以获取更多就绪事件, 其它时候, 异步等待的协程均挂起到等待列表, 不阻塞就绪协程的执行
实现了yield协程等待IO的简单调度版本, 但是也足够学习了
"""

from collections import deque
from select import select


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
        self._read_waiting = {}  # Tasks waiting to read
        self._write_waiting = {}  # Tasks waiting to write

    # Poll for I/O events and restart waiting tasks
    def _iopoll(self):
        rset, wset, eset = select(self._read_waiting, self._write_waiting, [])
        for r in rset:
            evt, task = self._read_waiting.pop(r)
            evt.handle_resume(self, task)
        for w in wset:
            evt, task = self._write_waiting.pop(w)
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
        self._read_waiting[fileno] = (evt, task)

    # Add a task to the write set
    def _write_wait(self, fileno, evt, task):
        self._write_waiting[fileno] = (evt, task)

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

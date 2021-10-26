#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
该实现中在Windows下模拟了socketpair()实现, 实际上3.5开始socketpair()已经支持Windows了
除了AF_INET, 还可以用AF_UNIX将socket实现为UNIX domain socket
select.select的参数只要实现了fileno方法或者存在fileno成员即可
"""
from queue import Queue
import socket
import os
import threading
import select
import time

class PollableQueue(Queue):


    def __init__(self):
        super().__init__()
        if os.name == 'posix':
            self._putsocket, self._getsocket = socket.socketpair()
        else:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(('127.0.0.1', 0))
            server.listen(1)
            self._putsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._putsocket.connect(server.getsockname())
            self._getsocket, addr = server.accept()
            server.close()

    def fileno(self):
        return self._getsocket.fileno()

    def put(self, msg):
        super().put(msg)
        self._putsocket.send(b'x')

    def get(self):
        self._getsocket.recv(1)
        return super().get()


def consumer(queues):
    while True:
        can_read, w, e = select.select(queues, [], [])
        for r in can_read:
            item = r.get()
            print('Got:', item)


def producer(queue):
    msg = 'msg'
    queue.put(msg)


q1 = PollableQueue()
q2 = PollableQueue()
q3 = PollableQueue()

t = threading.Thread(target=consumer, args=([q1, q2, q3], ))
t.daemon = True
t.start()

q1.put(1)
q1.put(2)
q3.put('hello')
q2.put(15)

time.sleep(0.5)
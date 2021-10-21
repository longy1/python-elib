#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
threading中提供了Thread对象, 创建Thread对象可以分配线程资源
使用多线程的方式:
    通过实例化Thread对象
    通过继承Thread类, 并定义run()方法
使用Thread.start()方法运行子线程
使用Thread.is_alive()判断线程状态
使用Thread.join()阻塞当前线程直到目标线程结束
使用守护线程来实现长时间运行或者后台任务
"""

import time, threading

def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(2)

t1 = threading.Thread(target=countdown, args=(1, ))
print('Start')
t1.start()
print(t1.is_alive())
time.sleep(3)
t1.join()
print('Terminate')


# deal block IO

class IOTask:

    def terminate(self):
        self._running = False

    def run(self, sock):
        sock.settimeout(5)
        while self._running:
            try:
                data = sock.recv(8192)
            except socket.timeout:
                continue

            # do sth with data
        return


# inherit Thread for concurrent

class TaskThread(threading.Thread):

    def __init__(self, n):
        self._n = n
        super().__init__()

    def run(self):
        while self._n > 0:
            print('T-minus', self._n)
            self._n -= 1
            time.sleep(1)

c = Task(5)
c.start()


# 
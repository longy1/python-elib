#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
使用全局变量
使用queue.Queue()
注意: Queue.size(), Queue.full(), Queue.empty()都不是线程安全的
"""

# 简单全局变量共享, 线程安全, 相当于非阻塞忙等待Event

import threading, time

def proc_high():
    global n
    while n == 0:
        pass
    print(f'start process n = {n}')
    time.sleep(3)
    print('high end')


def proc_low():
    global n
    if n == 0:
        time.sleep(3)
    n += 1
    print('low end')


n = 0
threading.Thread(target=proc_low).start()
threading.Thread(target=proc_high).start()


# 使用Queue安全共享, 使用Event终止

from queue import Queue
from threading import Thread, Event
import time

def consumer(q, e):
    while e.is_set():
        try:
            p = q.get()
            print(f'consumer {p}')
        except:
            pass

def producer(q, e):
    for i in range(10):
        time.sleep(1)
        q.put(i)
        print(f'producer {i}')
    e.clear()

q = Queue()
e = Event()
e.set()


t1 = Thread(target=consumer, args=(q, e))
t2 = Thread(target=producer, args=(q, e))

t1.start()
t2.start()
t1.join()
t2.join()
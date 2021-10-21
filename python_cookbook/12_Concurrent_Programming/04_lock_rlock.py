#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
基本的锁Lock()
重入锁RLock(), 可以安全地在一个获取锁的入口方法中反复获取相同的锁
在可以用Lock解决的事情上用Lock解决
用Semaphore可以更优雅地实现有限数目资源互斥访问
"""

# 一个线程安全的计数器
import threading

class SharedCounter:

    def __init__(self, initial_value = 0):
        self._value = initial_value
        self._lock = threading.Lock()

    def incr(self, delta=1):
        with self._lock:
            self._value += delta

    def decr(self, delta=1):
        with self._lock:
            self._value -= delta

sc = SharedCounter()

def add(counter):
    for i in range(1000000):
        counter.incr()

def remo(counter):
    for i in range(1000000):
        counter.decr()

t1 = threading.Thread(target=add, args=(sc, ))
t2 = threading.Thread(target=remo, args=(sc, ))
t1.start()
t2.start()
t1.join()
t2.join()

print(sc._value)
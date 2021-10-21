#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
如果直接获取所有锁, 那么可以排序这些锁, 并按顺序获取即可不死锁
若一个线程存在阶段性获取锁, 那么需要本地维护已获取的锁状态, 并且拒绝在获取到排序更大的锁后再获取更小的锁
"""

import threading, time
from contextlib import contextmanager

lock1 = threading.Lock()
lock2 = threading.Lock()

@contextmanager
def aquire(*locks):
    locks = sorted(locks, key=lambda x: id(x))
    try:
        for lock in locks:
            lock.acquire()
            time.sleep(1)
        yield
    finally:
        for lock in reversed(locks):
            lock.release()


def work1(*locks):
    with aquire(*locks):
        print('1')


def work2(*locks):
    with aquire(*locks):
        print('2')

t1 = threading.Thread(target=work1, args=(lock1, lock2))
t2 = threading.Thread(target=work2, args=(lock2, lock1))
t1.start()
t2.start()

t1.join()
t2.join()
print('ok')
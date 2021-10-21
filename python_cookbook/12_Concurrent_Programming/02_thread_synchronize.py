#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
简单的同步原语
Event对象
Condition对象
Semaphore对象
"""

# 使用Event判断线程已经启动

import time, threading

start_event = threading.Event()

def countdown(n):
    time.sleep(1)
    start_event.set()
    time.sleep(n)

t1 = threading.Thread(target=countdown, args=(4, ))

print('start')
t1.start()

start_event.wait()

print('start_event is OK')

t1.join()

print('t1 is done')


# 使用Condition同步两个线程

import time, threading

def wait(cond):
    print('wait start')
    with cond:
        cond.wait()
        print('wait end')

def signal(cond):
    print('signal start')
    with cond:
        time.sleep(4)
        cond.notify()
    print('signal end')

cv = threading.Condition()

t1 = threading.Thread(target=wait, args=(cv, ))
t2 = threading.Thread(target=signal, args=(cv, ))

print('main start')
t1.start()
time.sleep(1)
t2.start()

t1.join()
t2.join()

print('main end')


# 使用Semaphore同步

import threading, time

def wait(sem):
    print('wait start')
    sem.acquire()
    print('wait end')

def signal(sem):
    print('signal start and sleep')
    time.sleep(4)
    sem.release()
    print('signal end')

sem = threading.Semaphore(0)

t1 = threading.Thread(target=wait, args=(sem, ))
t2 = threading.Thread(target=signal, args=(sem, ))

print('main start')
t1.start()
t2.start()

t1.join()
t2.join()

print('main end')
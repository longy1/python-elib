#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a simple deadlock'

__author__ = 'Ethan Long'

import threading, time

def thread_1():
    with lock_1:
        print('t1 get lock_1')
        time.sleep(1)
        with lock_2:
            print('t1 get lock_2')
            time.sleep(2)

def thread_2():
    with lock_2:
        print('t2 get lock_2')
        time.sleep(1)
        with lock_1:
            print('t2 get lock_1')
            time.sleep(2)

lock_1 = threading.Lock()
lock_2 = threading.Lock()

t1 = threading.Thread(target=thread_1)
t2 = threading.Thread(target=thread_2)

print('start')

t1.start()
t2.start()

t1.join()
t2.join()

print('end')
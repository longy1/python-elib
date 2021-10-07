#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a simple reader-first implement of writer & reader problem '

__author__ = 'Ethan Long'

import threading, random, time

print('读者优先算法')

Rcount = 0
WriteMutex = threading.Semaphore(1)
RcountMutex = threading.Semaphore(1)

def writer():
    a = random.randint(0, 1000)

    WriteMutex.acquire()
    print(f'Writer {a} start writing.')

    time.sleep(3)
    print(f'Writer {a} finished writing.')
    WriteMutex.release()


def reader():
    a = random.randint(0, 1000)
    global Rcount

    RcountMutex.acquire()
    if Rcount == 0:
        WriteMutex.acquire()
    Rcount += 1
    RcountMutex.release()

    print(f'Reader {a} start reading.\n', end='')
    time.sleep(2)
    print(f'Reader {a} finished reading.\n', end='')

    RcountMutex.acquire()
    Rcount -= 1
    if Rcount == 0:
        WriteMutex.release()
    RcountMutex.release()
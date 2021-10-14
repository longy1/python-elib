#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'the test entry of reader & writer problem, using by rewriting writer and reader thread func'

__author__ = 'Ethan Long'

import threading, random
import semaphore_rw_rfirst_implement as implement

writer = implement.writer
reader = implement.reader

for i in range(1):
    pool = []
    for w in range(5):
        pool.append(threading.Thread(target=writer))
    for w in range(5):
        pool.append(threading.Thread(target=reader))

    print("program start")
    random.shuffle(pool)
    for t in pool:
        t.start()
    for t in pool:
        t.join()
    print("program terminated")
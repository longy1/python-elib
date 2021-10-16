#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a simple example of unsafe threads'

x = 0

def add():
	global x
	for i in range(10000):
		x += 1

from threading import Thread

t1 = Thread(target=add)
t2 = Thread(target=add)

t1.start()
t2.start()
t1.join()
t2.join()

print(x)
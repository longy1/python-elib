#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'first try threading'

__author__ = 'Ethan Long'

import threading
import time

def say_after(delay, what):
    print('begin', what)
    time.sleep(delay)
    print(what)

t1 = threading.Thread(target=say_after, args=(1, 't1'))
t2 = threading.Thread(target=say_after, args=(2, 't2'))


print(f"start at {time.strftime('%X')}")
t1.start()
t2.start()

t1.join()
print(f"t1 finished at {time.strftime('%X')}")
t2.join()

print(f"t2 finished at {time.strftime('%X')}")
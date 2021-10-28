#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
use yield to declare a generator
generator同样可以外部使用next()来迭代, 同样会抛出异常
for ... in 语句会帮助处理StopIteration异常
"""

def my_range(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

for i in my_range(1, 10, 2):
    print(i)
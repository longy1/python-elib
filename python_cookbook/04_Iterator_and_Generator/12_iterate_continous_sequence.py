#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
chain(*iters)不需要用list组合迭代器, 仅仅是分派迭代
"""

a = [1, 2, 3, 4]
b = ['x', 'y', 'z']

# trap
for i in a, b:
    print(i)

# right
import itertools

for i in itertools.chain(a, b):
    print(i)
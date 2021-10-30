#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
do like 'return r1, r2, r3'
will return a tuple.
"""

def ret():
    return 1, 2, 3

x = ret()
print(type(x))
print(x)
for i in x:
    print(i)
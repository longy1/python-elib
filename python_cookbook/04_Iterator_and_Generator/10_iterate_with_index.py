#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
use built-in func enumerate(iter, start=0)
"""

# basic use
s = 'dcbdad'
for k, v in enumerate(s, 1):
    print(k, v)

# avoid trap, enumerate has only 2 returns
s = [(1, 2), (2, 3), (4, 2)]
for k, (t1, t2) in enumerate(s):
    print(k, t1, t2)
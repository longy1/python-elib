#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
it's a trap that declare in func body
use default arg to bind ref var
"""

# trap
funcs = [lambda x: x+n for n in range(5)]
n = 7
for i in range(5):
    print(funcs[i](2))

# bind n
funcs = [lambda x, n=n: x+n for n in range(5)]
for i in range(5):
    print(funcs[i](3))
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
use itertools.islice(iter, start, end)
islice will consume iterator, it's a side effect
"""

def count(n):
    while True:
        yield n
        n += 1

import itertools

c = count(0)
for i in itertools.islice(c, 10, 20, 2):
    print(i)
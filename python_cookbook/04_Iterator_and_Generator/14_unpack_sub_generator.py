#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
repalce nested loop with yield from
"""
from collections.abc import Iterable

def flatten(items, ignore_types=(str, bytes)):
    for i in items:
        if isinstance(i, Iterable) and not isinstance(i, ignore_types):
            yield from flatten(i)
        else:
            yield i

items = [1, 2, [3, b'23432', 4, [5, 6], 7], 8, '1324']

for i in flatten(items):
    print(i)
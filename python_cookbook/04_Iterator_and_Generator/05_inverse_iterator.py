#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
use builts-in func reversed()
implement __reversed__() to return a iterator
"""

# reversed()
print(f'{"reversed":=^20}')
l = [5, 4, 3, 2, 1]
for i in reversed(l):
    print(i, end=' ')
print(l)


# __reversed__()
class Countdown:

    def __init__(self, start):
        self._start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        r = 1
        while r <= self._start:
            yield r
            r += 1

c = Countdown(5)
for i in reversed(c):
    print('j: ', end=' ')
    for j in reversed(c):
        print(j, end=' ')
    print('\ni: ', end=' ')
    print(i, end=' ')
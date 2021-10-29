#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
zip是会消耗的, 只能list化一次
"""

# zip(*iter)
xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]

for i in zip(xpts, ypts):
    print(i)

# zip() will stop when shortest iter over
a = 'abcd'
b = 'bcd'
c = 'cd'

for i in zip(a, b, c):
    print(i)


# itertools.zip_longest(*iters, fillvalue=Noe) will keep iterating
import itertools

a = 'abcd'
b = 'bcd'
c = 'cd'
for i in itertools.zip_longest(a, b, c, fillvalue='filled'):
    print(i)
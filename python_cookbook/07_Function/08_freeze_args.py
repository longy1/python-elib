#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
functools.partial() can freeze some args and return another callable object
which receive other args remain
if a position arg is replaced, other args behind it need to be provided by kwargs
"""

from functools import partial

# basic use
def span(a, b, c, d):
    print(a, b, c, d)

f1 = span
f2 = partial(span, 1, 2)
f3 = partial(span, c=2)
f4 = partial(span, 1, 2, 3, 4)

f1('a', 'b', 'c', 'd')
f2('c', 'd')
f3('a', 'b', d='d')  # can not use f3('a', 'b', 'd')
f4()
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
closure vars are usually used by inner func, but we can bind
some visit func to help showing them
"""

def closure(n=0):

    n = 0

    def inner():
        print(n)

    def setter(value):
        nonlocal n
        n = value

    def getter():
        return n

    inner.setter = setter
    inner.getter = getter

    return inner

c = closure(2)
c()
print(c.getter())
c.setter(3)
print(c.getter())
c()
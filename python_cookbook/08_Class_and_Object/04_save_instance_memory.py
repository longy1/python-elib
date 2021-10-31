#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
use class var __slots__ to define a class which can not define more 
instance vars not in __slots__, but it will save a mount of memory.
__slots__ can be used to restrict the members in class, it is just a side effect
"""

class Date:

    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def get(self):
        print('ok')

d = Date(2021, 2, 31)
d.get()
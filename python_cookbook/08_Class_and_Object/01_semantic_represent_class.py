#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
__repr__() is used by python cli to echo, it always satisfy eval(repr(x)) == x is True
__str__() is used by built-in func str() and print(), don't mix them. 
__getattr__() won't check members defined starts with '__', such as method __len__()
"""

class Pair:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Pair({self.x}, {self.y})'

    def __str__(self):
        return f'({self.x}, {self.y})'

pair = Pair(2, 3)
print(repr(pair))
print(str(pair))
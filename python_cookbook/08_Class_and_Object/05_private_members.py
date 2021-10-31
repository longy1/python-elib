#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
there is no real access control of class members in python

members start with _ is always treated as privite members by
coder, but not interpreter

members start with __ like __m need to be replaced by _[cls]__m,
if want to access it in outer space, but in inner space, just use __m
"""

class A:

    def __init__(self):
        self.__inter = 0

    def get_inter(self):
        return self.__inter


class B(A):

    def __init__(self):
        super().__init__()
        self.__inter = 2


a = A()
b = B()

print(a._A__inter)
print(a.get_inter())
print(b._A__inter)
print(b._B__inter)
print(b.get_inter())
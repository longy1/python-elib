#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
make args more semantic
"""

def foo(x, *, arg1, arg2, arg3):
    print(x, arg1, arg2, arg3)

foo(1, arg1=1, arg2=2, arg3=3)
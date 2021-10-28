#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
use dir() to show
"""

class A(type):

    pass

class B:
    
    pass

print([x for x in dir(A) if x not in dir(B)])
print([x for x in dir(B) if x not in dir(A)])
print([x for x in dir(A) if x in dir(B)])
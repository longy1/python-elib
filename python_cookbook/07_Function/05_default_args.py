#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
declare func like def func(arg=default) to declare a default arg
don't use changeable object as default
ref var default will clone itself and bind it to func object
use unuseful object to check whether the args is provided
"""

# default arg
def foo(x, y=1):
    return x ** y

print(foo(2, 3))
print(foo(3))

# changeable default trap
def foo(y=[]):
    y.append('trap')
    print(y)

foo([1, 2])
foo()
foo()

# ref var
g = 2
def foo(x=g):
    x += 1
    print(x)

foo()
foo()

# check args
_no_arg = object()
def foo(x, y=_no_arg):
    if y is _no_arg:
        print('No y')
    print(x, y)

foo(1, 2)
foo(3)
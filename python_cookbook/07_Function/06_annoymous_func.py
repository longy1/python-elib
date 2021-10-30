#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
declare annoymous func by lambda expression
avoid using lambda expression to create complex func
lambda is useful to provide 'key' arg in funcs like sort()
"""

# declare
foo = lambda x, y: x + y
print(foo(2, 3))

# in sort()
l = [(1, 'a'), (3, 'c'), (4, 'b'), (2, 'e')]
l.sort(key=lambda x: x[1])
print(l)
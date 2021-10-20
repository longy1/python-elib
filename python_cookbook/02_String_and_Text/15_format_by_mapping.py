#!/usr/bin/python3
# -*- coding: utf-8 -*-

'format(), format_map()'

__author__ = 'Ethan Long'

# format_map with vars()
a = 2
name = 'Alice'

print('{name} is {a}'.format_map(vars()))

# format_map with objects
class A():

    def __init__(self, name, n):
        self.name = name
        self.a = n

c = A('Alice', 2)
print('{name} is {a}'.format_map(vars(c)))

# define __missing__() for safety
class SafeDict(dict):

    def __init__(self):
        pass

    def __missing__(self, key):
        return f'{ {key} }'

d = SafeDict()
print('{name} is {a}'.format_map(d))
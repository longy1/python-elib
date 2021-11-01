#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
built-in func super() will return the caller's parent class object, using MRO
(method resolution order), and then we can use it's method. when given by
an arg 'type', super() will search __mro__ from the class given.
"""

# basic example
class A:

    def __init__(self, value):
        self.a = value


class B(A):

    def __init__(self, value1, value2):
        super().__init__(value1)
        self.b = value2


b = B(1, 2)
print(b.a)
print(b.b)


# cover special method
class Proxy:

    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, key):
        return getattr(self._obj, key)

    def __setattr__(self, key, value):
        if key.startswith('_'):
            super().__setattr__(key, value)
        else:
            setattr(self._obj, key, value)
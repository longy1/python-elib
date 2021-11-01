#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
defince base init class and inheritant it
"""

class BaseInit:

    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} args')

        for key, value in zip(self._fields, args):
            setattr(self, key, value)

        for key in self._fields[len(args):]:
            setattr(self, key, kwargs.pop(key))

        if kwargs:
            raise TypeError(f"Invalid arguments: {','.join(kwargs)}")


class Stock(BaseInit):

    _fields = ['name', 'age', 'price', 'money', 'hoppy']

    def __str__(self):
        return str([item for item in self.__dict__.items()])


s = Stock('Ethan', 'haha', '398.4', money='nothing', hoppy='cs')
print(s)
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
if want to check type like below, use class decorator

@Typed(int)
class TypedClass:
    ...

"""

class Despriptor:

    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


def typed(expected_type):

    def decorator(cls):
        super_set = cls.__set__

        def __set__(self, instance, value):
            if not isinstance(value, expected_type):
                raise TypeError(f'Expected {expected_type}')
            super_set(self, instance, value)

        cls.__set__ = __set__

        return cls

    return decorator


@typed(int)
class Integer(Despriptor):

    pass


class Stock:

    shares = Integer('shares')

    def __init__(self, shares):

        self.shares = shares


s = Stock(shares=123)
print(s.shares)
try:
    s.shares = 1.2
except TypeError as e:
    print('Error:', e)
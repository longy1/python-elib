#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
use descriptor to override simple getattr, then cache compute result
"""

# changeable implementation
class lazy_attr:

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if not instance:
            return self

        result = self.func(instance)
        setattr(instance, self.func.__name__, result)
        return result


# unchangeable implementation
def unchangeable_lazy_property(func):

    name = '_lazy_' + func.__name__
    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            result = func(self)
            setattr(self, name, result)
            return result

    return lazy

import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    @lazy_attr
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @unchangeable_lazy_property
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius



    

c = Circle(3)
print(c.area)
print(c.perimeter)
print(c.area)
c.perimeter = 23
print(c.perimeter)
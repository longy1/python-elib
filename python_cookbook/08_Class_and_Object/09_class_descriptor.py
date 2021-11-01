#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
A descriptor can provide more hook-like operations on attr, but keep
new class simple and graceful by reusing same descriptor
"""

# magic

class Intenger:

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        print(f'Get {self.name}')
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print(f'Set {self.name} to {value}')
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:

    x = Intenger('x')
    y = Intenger('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


print(f"{'Magic':=^20}")
p = Point(1, 2)
p.x = 3
p.y = 4
print(p.x, p.y)
print(Point.x)


# more magic

class Typed:

    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_

    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.type_):
            raise TypeError(f'Expected {self.type_}')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


# decorator
def type_assert(**kwargs):

    def wrapper(cls):
        for name, type_ in kwargs.items():
            setattr(cls, name, Typed(name, type_))
        return cls

    return wrapper


@type_assert(name=str, age=int, price=float)
class Product:

    def __init__(self, name, age, price):
        self.name = name
        self.age = age
        self.price = price

    def __str__(self):
        return f'Product(name={self.name}, age={self.age}, price={self.price})'


print(f"{'More magic':=^20}")
p = Product('haha', 18, 20.0)
print(p)
try:
    p.name = 123
except TypeError as e:
    print(e)

try:
    p.age = 'age'
except TypeError as e:
    print(e)

try:
    p.price = 123
except TypeError as e:
    print(e)
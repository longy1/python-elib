#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
it is better to use descriptor to implement type constraint
"""

# subclass implement
class Despriptor:

    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Typed(Despriptor):

    expected_type = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f'Expected {str(self.expected_type)}')
        super().__set__(instance, value)


class Unsigned(Despriptor):

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        super().__set__(instance, value)


class MaxSized(Despriptor):

    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('Missing size option')
        super().__init__(name, **opts)

    def __set__(self, instance, value):
        if len(value) > self.size:
            raise ValueError(f'Size must be < {str(self.size)}')
        super().__set__(instance, value)


class Integer(Typed):

    expected_type = int


class UnsignedInteger(Integer, Unsigned):

    pass


class Float(Typed):

    expected_type = float


class UnsignedFloat(Float, Unsigned):

    pass


class String(Typed):

    expected_type = str


class SizedString(String, MaxSized):

    pass


class Stock:
    """
    it is a little complex to provide every name str for Descriptor
    """
    name = SizedString('name', size=10)
    shares = UnsignedInteger('shares')
    price = UnsignedFloat('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


s = Stock('Ethan', 123, 2.0)
print(s.name, s.shares, s.price)

try:
    s = Stock(123, 123, 123.0)
except TypeError as e:
    print('Error:', e)


# use metaclass to auto bind str 'name'
class CheckedMeta(type):

    def __new__(cls, cls_name, bases, methods):
        for key, value in methods.items():
            if isinstance(value, Despriptor):
                value.name = name
            return type.__new__(cls, cls_name, bases, methods)


class StockM(metaclass=CheckedMeta):
    """
    compare to Stock, no need to init Descriptor
    """
    name = SizedString(size=10)
    shares = UnsignedInteger()
    price = UnsignedFloat()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


try:
    s = StockM('Ethan', 123, 123)
except TypeError as e:
    print('Error:', e)
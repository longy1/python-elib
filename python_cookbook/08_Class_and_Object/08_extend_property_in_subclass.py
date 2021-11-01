#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
make it clear whether we want to override one of three property method
or all the property method in parent class
"""

# extend whole property
class Person:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError('Can not delete attribute')


class SubPerson(Person):
    """use parent's __init__()"""
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)

print('override all')
s = SubPerson('Guido')
print(s.name)
s.name = 'haha'
print(s.name)


# override only getter

class SubPerson(Person):

    @Person.name.getter
    def name(self):
        print('Getting name')
        return super().name

print('override only getter')
s = SubPerson('Guido')
print(s.name)
s.name = 'haha'
print(s.name)
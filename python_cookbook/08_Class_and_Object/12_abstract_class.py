#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
abc and collections.abc modules provide ways to define abstract class and
abstract method. 
"""

# a simple abstract class with some abstract interface
from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):

    @abstractmethod
    def read(self, max_bytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


# we can use register() to implement abs class
import io

IStream.register(io.IOBase)

f = open('foo.txt', 'w')
print(isinstance(f, IStream))
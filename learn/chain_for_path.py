#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Ethan Long'

class Chain(object):
    def __init__(self, text=''):
        self._text = text

    def __getattr__(self, text):
        return Chain(f'{self._text}/{text}')

    def __str__(self):
        return self._text

    __repr__ = __str__

a = Chain('www.baidu.com').path1.path2.path3
print(a)
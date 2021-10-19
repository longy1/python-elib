#!/usr/bin/python3
# -*- coding: utf-8 -*-

'use re.compile(), then use pattern.match(), pattern.findall(), pattern.finditer()'

__author__ = 'Ethan Long'

import re

# 使用compile()可以缓存模式
pattern = re.compile(r'\d+/\d+/\d+')

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

# return None because match() compare str from the begining.
print('pattern.match(text):', pattern.match(text))

# match return a object, use group() and groups() to get catched element
m = pattern.match('2020/01/03')
print('m:', m)
print('m.group(0):', f'{m.group(0)}')

# findall return a list of match pattern
print('pattern.findall(text):', pattern.findall(text))

# use () to catch, will return catched element
pattern = re.compile(r'(\d+)/(\d+)/(\d+)')
print('pattern.findall(text):', pattern.findall(text))

# use finditer() to get iterator
iterator = pattern.finditer(text)

for m in iterator:
    print(m.groups())
#!/usr/bin/python3
# -*- coding: utf-8 -*-

'use ljust(), rjust(), center(), format'

__author__ = 'Ethan Long'

text = 'Hello World'

print([text.ljust(20, ' ')])
print([text.rjust(20, '=')])
print([text.center(20, '*')])

# use format
print([format(text, '>20')])
print([format(text, '<20')])
print([format(text, '^20')])

# use str.format
text = '{:*>20}, {:=^20}'
print([text.format('Hello', 'World')])

# rouding while formating
text = '{:*>20.2f}, {:=^20.4f}'
print([text.format(123.3249234987, 32.324923874)])
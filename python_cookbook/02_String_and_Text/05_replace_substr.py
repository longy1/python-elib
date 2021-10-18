#!/usr/bin/ python3
# -*- coding: utf-8 -*-

'str.replace(), re.sub()'

__author__ = 'Ethan Long'

# use replace() to replace one pattern
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', '2015'))

# use re.sub() for complex replacing
import re

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
rtext = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(rtext)

# compile re str to reuse
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
rtext = datepat.sub(r'\3-\1-\2', text)
print(rtext)

# use refactor func to build substr
def refactor(m):
    print('pre-hook:', m.group(1))
    return f'{m.group(3)}-{m.group(1)}-{m.group(2)}'

rtext = datepat.sub(refactor, text)
print(rtext)

# use named group in re
pattern = re.compile(r'(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)')
rtext = pattern.sub(r'\g<year>-\g<month>-\g<day>', text)
print(rtext)

# use subn to count replacement
rtext, n = pattern.subn(r'\g<year>-\g<month>-\g<day>', text)
print(n)
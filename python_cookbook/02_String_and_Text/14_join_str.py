#!/usr/bin/python3
# -*- coding: utf-8 -*-

'str.join(), +, format, f-string, print(sep="s")'

__author__ = 'Ethan Long'

# join()
a = ['Hello', 'World', '!']
print(' '.join(a))

# +
s1, s2 = 'a', 'b'
print(s1 + s2)

# format
print('{}, {}'.format(s1, s2))

# f-string
print(f'{s1}, {s2}')

# seq=
print(s1, s2, sep=', ')

# DONT USE iter and + like below
s = ''
for i in a:
    s += i
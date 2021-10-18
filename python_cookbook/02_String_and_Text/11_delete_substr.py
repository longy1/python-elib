#!/usr/bin/ python3
# -*- coding: utf-8 -*-

'strip, lstrip, rstrip, replace'

__author__ = 'Ethan Long'

# default
text = '    alfkjklafjkl    '

print([text.strip()])
print([text.lstrip()])
print([text.rstrip()])

# customize
text = '...??..faklfjalk????'

print([text.strip('?')])
print([text.lstrip('.')])
print([text.rstrip('?')])
#!/usr/bin/python3
# -*- coding: utf-8 -*-

're, scanner'

__author__ = 'Ethan Long'

import re

text = 'foo = 23 + 42 * 10'

wanted_tokens = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),
          ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]

# how to get wanted_tokens

# define pattern
NAME = r'(?P<NAME>[a-zA-z_][a-zA-z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

scanner = master_pat.scanner('foo = 42')
s = scanner.match()
print(s.group())
s = scanner.match()
print(s.group())
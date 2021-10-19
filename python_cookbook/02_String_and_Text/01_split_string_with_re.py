#!/usr/bin/python3
# -*- coding: utf-8 -*-

'split str with re'

__author__ = 'Ethan Long'

import re

line = 'asdf fjdk; afed, fje|k,asdf, foo|'

l = re.split(r'[;,\s]\s*', line)
print(l)

l = re.split(r'(;|\||,|\s)\s*', line)
print(l)

l = re.split(r'(?:;|\||,|\s)\s*', line)
print(l)
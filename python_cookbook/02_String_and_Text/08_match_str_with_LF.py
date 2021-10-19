#!/usr/bin/python3
# -*- coding: utf-8 -*-

'use (?:\n|.)* or re.DOTALL'

__author__ = 'Ethan Long'

text = '''/* line 1, 
line 2 */
'''

import re

# wrong match, return []
print(re.findall(r'/\*.*\*/', text))

# true match
print(re.findall(r'/\*((?:.|\n)*?)\*/', text))

# true match using re.DOTALL
pat = re.compile(r'/\*((?:.*?))\*/', re.DOTALL)
print(pat.findall(text))
#!/usr/bin/python3
# -*- coding: utf-8 -*-

r'use \d, \w, \u'

__author__ = 'Ethan Long'

import re

text = '\u0032\u0034\u0045'

# \d
print(re.findall(r'\d+', text))

# \w
print(re.findall(r'\w+', text))

# \u
print(re.findall(r'\u0032\u0034', text))
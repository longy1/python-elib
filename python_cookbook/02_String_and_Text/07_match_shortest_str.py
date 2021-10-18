#!/usr/bin/ python3
# -*- coding: utf-8 -*-

'add ? after *'

__author__ = 'Ethan Long'

import re

# * is greed
text = 'Computer says "no." Phone says "yes."'
print(re.findall('".*"', text))

# *? is not greed
print(re.findall('".*?"', text))
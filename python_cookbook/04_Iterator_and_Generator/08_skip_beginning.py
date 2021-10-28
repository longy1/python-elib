#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
itertools.dropwhile() for unknown counts of line
itertools.islice() for certainly lines
"""

# avoid annotation at the beginning
from itertools import dropwhile

with open('path/file') as f:
    for line in dropwhile(lambda line: not line.startwith('#'), f):
        print(line, end='')


# avoid n rows at the beginning
from functools import islice

with open('path/file') as f:
    for line in islice(f, 3, None):  # will avoid first 3 lines
        print(line, end='')
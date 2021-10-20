#!/usr/bin/python3
# -*- coding: utf-8 -*-

'textwrap'

__author__ = 'Ethan Long'

import textwrap

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

# get list
print('get list'.center(40, '*'))
print(textwrap.wrap(s, 40))

# get str
print('get str'.center(40, '*'))
print(textwrap.fill(s, 40))

# initial_indent
print('initial_indent'.center(40, '*'))
print(textwrap.fill(s, 40, initial_indent=' '*4))

# subsequent_indent
print('subsequent_indent'.center(40, '*'))
print(textwrap.fill(s, 40, subsequent_indent=' '*4))

# get CLI width, must be used in Terminal
import os
print(os.get_terminal_size().columns)
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
encapsulate generator into a class
"""

from collections import deque

class LineHistoryGenerator:

    def __init__(self, lines, his_len=3):
        self.lines = lines
        self.history = deque(maxlen=his_len)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()

with open('path/file') as f:
    lines = LineHistoryGenerator(f)
    for line in lines:
        if 'python' in line:
            for lineno, hline in lines.history:
                print(f'{lineno}:{hline}')
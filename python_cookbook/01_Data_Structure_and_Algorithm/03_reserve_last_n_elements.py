#!/usr/bin/ python3
# -*- coding: utf-8 -*-

# how to
from collections import deque

def search(lines, pattern, history=5):
    prev_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, prev_lines
        prev_lines.append(line)
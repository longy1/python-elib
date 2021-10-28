#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
iterate manually by next()
"""

# try
def manual_iter():
    with open('path/file') as f:
        try:
            while Ture:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass

# default next
def manual_iter():
    with open('path/file') as f:
        while True:
            line = next(f, None)
            if line is None:
                break
            print(line, end='')
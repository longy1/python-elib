#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
use generator to process by single step
"""

import os
import fnmatch
import gzip
import bz2
import re

def gen_find(filepat, top):
    """
    get file fits filepat, from recursive traver from top 
    """
    # os.walk(top) return (dirpath, dirnames, filenames)
    path = os.path.abspath(top)

    for dirpath, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, filepat):
            yield os.path.join(dirpath, filename)

def gen_opener(filenames):
    """
    get file descriptor, distinguishing extension
    """
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt', encoding='utf8')
        yield f
        f.close()

def gen_concatenate(files):
    """
    tranfer file to lines
    """
    for file in files:
        yield from file

def gen_grep(pattern, lines):
    """
    match pattern in lines
    """
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line

pattern = 'class '

files = gen_find('*.py', 'S:/PythonCode/python_elib')
fds = gen_opener(files)
lines = gen_concatenate(fds)
match_lines = gen_grep(pattern, lines)

for i in filter(lambda s: s.startswith('class '), match_lines):
    print(i.strip())
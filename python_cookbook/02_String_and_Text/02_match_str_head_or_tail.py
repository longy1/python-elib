#!/usr/bin/ python3
# -*- coding: utf-8 -*-

'str.startswith(), str.endswith()'

__author__ = 'Ethan Long'

files = ['a.py', 'b.bin', 'log_time.log', 'Makefile', 'spam.c', 'lib.py']

py_files = [x for x in files if x.endswith('py')]
print(py_files)

# 如果传多个匹配对象, 需要转化为tuple
match = [x for x in files if x.endswith(('.py', '.c', '.bin'))]
print(match)

head = [x for x in files if x.startswith('l')]
print(head)
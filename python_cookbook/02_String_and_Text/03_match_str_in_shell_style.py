#!/usr/bin/ python3
# -*- coding: utf-8 -*-

'use fnmatch'
# Shell通配符
# * 匹配所有
# ? 匹配任何单个字符
# [seq] 匹配seq中任何字符
# [!seq] 匹配不在seq中任何字符

__author__ = 'Ethan Long'

from fnmatch import fnmatch, fnmatchcase

files = ['a.py', 'b.bin', 'log_time.log', 'c.PY', 'Makefile', 'spam.c', 'lib.py']

# fnmatch大小写不敏感
py_file = [x for x in files if fnmatch(x, '*.py')]
print(py_file)

# fnmatchcase大小写敏感
py_file = [x for x in files if fnmatchcase(x, '*.py')]
print(py_file)

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

addr_5_clark = [x for x in addresses if fnmatchcase(x, '5*CLARK*')]
print(addr_5_clark)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class bytearray([source[, encoding[, errors]]])'
'返回可变的类bytes对象, 与bytes有相同的方法'

a = bytearray(b'falkjflakj')
a[2] = 122
print(a)
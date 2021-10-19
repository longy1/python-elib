#!/usr/bin/python3
# -*- coding: utf-8 -*-

'class slice(stop)'
'class slice(start, stop[, step])'
'返回可用于__getitem__()方法的slice对象'
'可访问slice.start, slice.stop, slice.step'

s = slice(0, None, 2)
a = [1, 2, 3, 4, 5]
print(a[s])
print(s.step)
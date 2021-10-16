#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'iter(object[, sentinel])'
'若无实参sentinel, 则调用object的__iter__()方法, 不存在则调用__getitem__()方法'
'若有实参sentinel, 则object必须是callable对象, 并且每次调用next时会调用一次object, 失败则返回sentinel'

# 使用iter构建块读取器
from functools import partial
with open('mydata.db', 'rb') as f:
	for block in iter(partial(f.read, 64), b'')
		process_block(block)
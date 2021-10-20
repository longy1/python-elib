#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
2.20 字节字符串上的字符串操作
Bytes和ByteArray都可以用re匹配, 但是re需要编译字节字符串
注意匹配单个结果返回的是整数, 即ord()的结果, 需要用chr()转换为字节
"""

import re

data = b'Hello World'

pat = re.compile(b'world', flags=re.IGNORECASE)
seq = pat.findall(data)
print(seq)
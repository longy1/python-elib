#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'any(iterable)'
'若迭代对象中任意元素为真, 则返回True'

# 等价于
def any(iter):
    for i in iter:
        if i:
            return True
    return False
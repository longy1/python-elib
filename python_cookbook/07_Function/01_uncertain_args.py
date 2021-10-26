#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
*args用于接受任意数量的参数, 以满足所有参数
*只能放在位置参数的末尾, 后面的参数均为关键字参数
**kw用于接受任意数量的关键字参数
*args, **kwargs可以接受任意参数
"""

# 注意*rest会被当作元组而不是list
def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))

print(avg(1, 2, 5, 4))


# **kw会被当作dict
import html

def make_element(name, value, **kwargs):

    kv = {f' {x[0]}={x[1]}' for x in kwargs.items()}
    attrs = ''.join(kv)
    element = f'<{name}{attrs}>{html.escape(value)}</{name}>'
    return element

print(make_element('item', 'Alibaba', size='large', quantity=6))
print(make_element('p', '<spam>'))
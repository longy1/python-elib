#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'zip(*iterables)'
'创建聚合来自每个可迭代对象中的元素的迭代器'
'终止于某一个迭代器用尽'

def zip(*iterables):
    sentinel = object()
    iterators = [iter(it) for it in iterables]

    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)

''
x = [1, 2, 3]
y = [4, 5, 6, 7]

print(list(zip(x, y)))
print(list(zip(*zip(x, y))))
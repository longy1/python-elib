#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
implement __iter__() to return iterator object
"""

# 可迭代对象只需实现__next__(), 此例借助了list的实现
class Node:

    def __init__(self, value):
        self._value = value
        self._children = []

    def add_child(self, node):
        self._children.append(node)

    def __repr__(self):
        return f'Node({self._value})'

    def __iter__(self):
        return iter([self] + self._children)


if __name__ == '__main__':

    root = Node(1)
    root.add_child(Node(2))
    root.add_child(Node(3))

    for i in root:
        print(i)
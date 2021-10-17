#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class bool(x)'
'使用真值测试过程, 决定返回True还是False'
'若x.__bool__()定义了, 则返回, 否则返回x.__len__()'

# 测试覆盖性
class A(object):
    """docstring for A"""
    def __init__(self, arg):
        super(A, self).__init__()
        self.arg = arg
        
    # def __bool__(self):
    #     return False

    def __len__(self):
        return 1

a = A(1)
print(bool(a))
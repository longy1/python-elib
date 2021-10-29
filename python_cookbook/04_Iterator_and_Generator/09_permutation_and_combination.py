#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
itertools.permutations(iter[, len])
itertools.combinations(iter, len)
itertools.combinations_with_replacement(iter, len)
"""

import itertools

# permutation
print('permutaion')
l = 'dbca'
for i in itertools.permutations(l, 3):
    print(''.join(i))

# combination
print('combination')
l = 'dbca'
for i in itertools.combinations(l, 2):
    print(''.join(i))

# combination with replacement, means filtered cartesian product
print('combination with repeat')
l = 'dbca'
for i in itertools.combinations_with_replacement(l, 2):
    print(''.join(i))
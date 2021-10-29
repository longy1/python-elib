#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
heapq.merge(*iter) will create a heap with capacity equals iter's length
heapq.merge(*iter) return a generator, means saving memory
"""

import heapq

# simple example
a = [1, 2, 6, 8, 9]
b = [3, 5, 9, 12]

for i in heapq.merge(a, b):
    print(i)


# merge sorted file
with open('sorted_file_1', 'rt') as file1, \
    open('sorted_file_2', 'rt') as file2, \
    open('merged_file', 'wt') as outf:

    for line in heapq.merge(file1, file2):
        outf.write(line)
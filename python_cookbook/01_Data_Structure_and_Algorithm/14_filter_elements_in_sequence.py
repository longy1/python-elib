#!/usr/bin/python3
# -*- coding: utf-8 -*-

'filter an iter by another iter'

__author__ = 'Ethan Long'

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
print([x for x in zip(addresses, counts) if x[1] > 5])
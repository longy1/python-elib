#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
use tag attr to switch format chosen
"""

_formats = {
    'ymd' : '{d.year}-{d.month}-{d.day}',
    'mdy' : '{d.month}/{d.day}/{d.year}',
    'dmy' : '{d.day}/{d.month}/{d.year}'
    }

class Date:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, tag=''):
        if tag == '':
            tag = 'ymd'
        return _formats[tag].format(d=self)

d = Date(2021, 10, 31)
print(format(d))
print(format(d, 'mdy'))
print(format(d, 'dmy'))
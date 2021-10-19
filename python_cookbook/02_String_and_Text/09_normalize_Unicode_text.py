#!/usr/bin/python3
# -*- coding: utf-8 -*-

'use unicodedata.normalize()'

__author__ = 'Ethan Long'

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

print(s1 == s2)

import unicodedata

s3 = unicodedata.normalize('NFC', s1)
s4 = unicodedata.normalize('NFC', s2)
print(s3 == s4)

s3 = unicodedata.normalize('NFD', s1)
s4 = unicodedata.normalize('NFD', s2)
print(s3 == s4)
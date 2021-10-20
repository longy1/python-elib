#!/usr/bin/python3
# -*- coding: utf-8 -*-

'html'

__author__ = 'Ethan Long'

import html
s = 'Elements are written as "<tag>text</tag>".'

safe_s = html.escape(s)
print(safe_s)

unsafe_s = html.unescape(safe_s)
print(unsafe_s)
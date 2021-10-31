#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
a closure looks like a netesd func, outer func return a inner func,
and inner func will remember outer vars, it's powerful
"""

def outer(x):
    x = x
    def inner(y):
        nonlocal x
        x += 1
        return y ** x
    return inner  # this return will remember given x

f = outer(3)
print(f(2))
print(f(3))

# closure can be used to replace simple class
from urllib.request import urlopen

class UrlTemplate:

    def __init__(self, template):
        self._template = template

    def open(self, **kwargs):
        return urlopen(self._template.format_map(kwargs))

yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo.open(names='IBM,AAPL,FB', fields='sl1c1v'):
    print(line.decode())

# use closure to replace class above

def UrlTemplate(template):

    def open(**kwargs):
        return urlopen(template.format_map(kwargs))

    return open
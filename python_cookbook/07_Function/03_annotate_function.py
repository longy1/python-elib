#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
func annotation is just like code annotation, the interpreter won't check them.
help() will show func annotation info.
func annotation is saved in __annotations__ attr.
"""

def sum(x: int, y: int) -> int:
    return x + y

print(help(sum))
print(sum(1, 2))
print(sum('a', 'b'))
print(sum.__annotations__)
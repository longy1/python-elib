#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'definition of decorator'

__author__ = 'Ethan Long'

import functools

def dec(text):
    def wrap(func, text=None):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print(f'Call {func.__name__}{" " + text if text else ""}')
            return func(*args, **kw)
        return wrapper

    if callable(text):
        return wrap(text)
    else:
        def decorator(func):
            return wrap(func, text)
        return decorator

# means my_sum = dec('haha')(my_sum), dec need to return a func
@dec('haha')
def my_sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(my_sum(1, 2, 3))
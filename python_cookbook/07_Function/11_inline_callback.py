#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
define yield event
define sheduler
define procedure
"""

class YieldEvent:

    def __init__(self, func, args):
        self.func = func
        self.args = args

def apply_async(func, args, *, callback):

    result = func(*args)

    callback(result)

from functools import wraps
from queue import Queue

def inlined_async(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        f = func(*args, **kwargs)
        result_queue = Queue()
        result_queue.put(None)

        while True:
            result = result_queue.get()
            try:
                event = f.send(result)
                apply_async(event.func, event.args, callback=result_queue.put)
            except StopIteration:
                break

    return wrapper

def add(x, y):
    return x + y

@inlined_async
def test():
    r = yield YieldEvent(add, (2, 3))
    print(1, r)
    r = yield YieldEvent(add, ('ab', 'cd'))
    print(2, r)
    for i in range(10):
        r = yield YieldEvent(add, (i, i))
        print(3+i, r)

test()
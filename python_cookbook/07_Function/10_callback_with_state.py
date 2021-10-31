#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
use class or closure or generator to remember some states
"""

# we may define a callback func like this
# but callback can only receive one arg, we may lost state
def apply_async(func, args, *, callback):
    result = func(*args)

    callback(result)

# use class
class Context:

    def __init__(self, start=0):
        self.seq = start

    def handle_resume(self, result):
        print(f'[{self.seq}] Got: {result}')
        self.seq += 1

context = Context()

apply_async(lambda x, y: x + y, (1, 3), callback=context.handle_resume)
apply_async(pow, (2, 4), callback=context.handle_resume)

# use closure
def context(start=0):
    seq = start

    def handle_resume(result):
        nonlocal seq
        print(f'[{seq}] Got: {result}')
        seq += 1

    return handle_resume

handle = context()
apply_async(lambda x, y: x + y, (1, 3), callback=handle)
apply_async(pow, (2, 4), callback=handle)

# use generator
def handle_resume(start=0):
    seq = start
    while True:
        result = yield seq
        print(f'[{seq}] Got: {result}')
        seq += 1

handle = handle_resume()
handle.send(None)  # init it
apply_async(lambda x, y: x + y, (1, 3), callback=handle.send)
apply_async(pow, (2, 4), callback=handle.send)
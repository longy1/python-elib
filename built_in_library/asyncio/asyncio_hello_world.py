#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
async def will define a async func.

await will block it self, but won't block outer func.
await can be used to start a async func, but may block other coroutines.

asyncio.run(async_func) starts a new async procedure
async func can not be called directly.

asyncio.create_task(async_func(*args, **kwargs)) will return a awaitable
Task object, await Task will not blocking other coroutines.
"""

import asyncio
import time

async def say_after(delay, what):
    print('begin', what)
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello task1'))

    task2 = asyncio.create_task(
        say_after(2, 'hello task2'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    print('await')
    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
print('outer')
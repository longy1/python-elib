#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
first use of asyncio
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
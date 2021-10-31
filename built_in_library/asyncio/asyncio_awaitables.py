#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
An awaitable object can be used in an await expression.
coroutines, Tasks, Futures are awaitable objects.
"""

# await coroutines
import asyncio, time

async def nested(n):
    await asyncio.sleep(n)
    return f'Nested {n}'

async def main():

    # nothing wil happen, this expression just return a coroutine object
    nested(1)  # cpython will give a RuntimeWarning

    print(f"started at {time.strftime('%X')}")
    await nested(1)
    await nested(2)
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())


# await Task, which is returned by asyncio.create_task()

async def nested(n):
    await asyncio.sleep(n)
    return f'Nested {n}'

async def main():

    task1 = asyncio.create_task(nested(1))
    task2 = asyncio.create_task(nested(2))

    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())


# Future is a low-level awaitable object that represents an eventual result

# simple example
async def main():
    await function_that_returns_a_future_object()

    # this is also valid:
    await asyncio.gather(
        function_that_returns_a_future_object(),
        some_python_coroutine()
    )

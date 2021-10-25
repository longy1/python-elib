#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
yield声明的函数会变成生成器
yield后接表达式作为一次next()的返回值
yield from可以将返回委托给另一个迭代器
.send()可以为yield赋予返回值
"""

# 一个轮询的count队列调度

def countdown(n):
    while n > 0:
        print('T-minus', n)
        yield
        n -= 1
    print('Over')

def countup(n):
    x = 0
    while x < n:
        print('Counting up', x)
        yield
        x += 1

from collections import deque

class TaskScheduler:

    def __init__(self):
        self._task_queue = deque()

    def new_task(self, task):
        self._task_queue.append(task)

    def run(self):
        while self._task_queue:
            task = self._task_queue.popleft()
            try:
                next(task)
                self._task_queue.append(task)
            except StopIteration:
                pass

sched = TaskScheduler()
sched.new_task(countup(10))
sched.new_task(countdown(5))
sched.new_task(countdown(15))
sched.run()


# 一个类Actor模型的调度

from collections import deque

class ActorScheduler:

    def __init__(self):
        self._actors = {}
        self._msg_queue = deque()

    def new_actor(self, name, actor):
        self._actors[name] = actor
        self._msg_queue.append((actor, None))

    def send(self, name, msg):
        actor = self._actors.get(name)
        if actor:
            self._msg_queue.append((actor, msg))

    def run(self):
        while self._msg_queue:
            actor, msg = self._msg_queue.popleft()
            try:
                actor.send(msg)
            except StopIteration:
                pass


if __name__ == '__main__':
    def printer():
        while True:
            msg = yield
            print(f'Printer: {msg}')

    def counter(sched):
        while True:
            n = yield
            if n == 0:
                break
            sched.send('printer', n)
            sched.send('counter', n-1)

    sched = ActorScheduler()
    sched.new_actor('printer', printer())
    sched.new_actor('counter', counter(sched))

    sched.send('counter', 100)
    sched.run()
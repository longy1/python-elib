#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
该模块中的实现可以作为Observer模式的Python实现
"""

from collections import defaultdict
from contextlib import contextmanager

class Exchange:

    def __init__(self):
        self._subscribers = set()

    def attach(self, task):
        self._subscribers.add(tast)

    def detach(self, task):
        self._subscribers.remove(tast)

    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)

    @contextmanager
    def subscribe(self, *tasks):
        for task in tasks:
                self.attach(task)
        try:
            yield
        finally:
            for task in tasks:
                self.detach(task)


_exchanges = defaultdict(Exchange)

def get_exchange(name):
    return _exchanges[name]


# 使用用例

def Task:

    def send(self, msg):
        pass

task_a = Task()
task_b = Task()

exc = get_exchange('name')

exc.attach(task_a)
exc.attach(task_b)

exc.send('msg1')
exc.send('msg2')

exc.detach(task_a)
exc.detach(task_b)
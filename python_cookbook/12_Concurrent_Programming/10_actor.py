#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Actor作为一个并发对象, 管理线程
"""

# 使用Queue定义一个Actor

from threading import Thread, Event
from queue import Queue
import time

class ActorExit(Exception):
    pass


class Actor:

    def __init__(self):
        self._mailbox = Queue()

    def send(self, msg):
        self._mailbox.put(msg)

    def recv(self):
        msg = self._mailbox.get()
        if msg is ActorExit:
            raise ActorExit()
        return msg

    def close(self):
        self.send(ActorExit)

    def start(self):
        # 未处理重复start的调用
        self._terminated = Event()
        t = Thread(target=self._bootstrap)
        t.daemon = True
        t.start()

    def _bootstrap(self):
        try:
            self.run()
        except ActorExit:
            pass
        finally:
            self._terminated.set()
        
    def join(self):
        self._terminated.wait()

    def run(self):
        while True:
            msg = self.recv()



# 使用简单的EchoActor

class EchoActor(Actor):

    def run(self):
        while True:
            msg = self.recv()
            print(f'Got msg: {msg}')


a = EchoActor()
a.start()
a.send('haha')
a.send('fjaklfj')
time.sleep(2)
a.close()
a.join()


# 使用复杂的DispatchActor

class DispatchActor(Actor):

    def run(self):
        while True:
            tag, *payload = self.recv()
            getattr(self, 'dispatch_' + tag)(*payload)

    def dispatch_add(self, a, b):
        print(f'Add {a} + {b} = {a+b}')

    def dispatch_echo(self, msg):
        print(f'Got {msg}')


da = DispatchActor()
da.start()
da.send(('add', 2, 3))
da.send(('echo', 'fjaklfjalkjf'))
da.close()
time.sleep(2)
da.join()


# 执行任意任务的Actor
class Result():

    def __init__(self):
        self._evt = Event()
        self._result = None


    def set_result(self, val):
        self._result = val
        self._evt.set()

    def result(self):
        self._evt.wait()
        return self._result


class GeneralActor(Actor):

    def submit(self, func, *args, **kwargs):
        r = Result()
        self.send((func, args, kwargs, r))
        return r

    def run(self):
        while True:
            func, args, kwargs, r = self.recv()
            r.set_result(func(*args, **kwargs))


worker = GeneralActor()
worker.start()
r = worker.submit(pow, 2, 3)
worker.close()
worker.join()
print(r.result())
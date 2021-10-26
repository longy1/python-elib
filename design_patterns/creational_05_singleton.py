#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
线程安全的singleton
"""

# 立即加载, 基于__new__(), 在类创建时便已经实例化, 不需要保证线程安全也线程安全
class Singleton:

    _instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

class AFactory(Singleton):
    pass


class BFactory(Singleton):
    pass


a = AFactory()
b = AFactory()
print(id(a), id(b), id(a)==id(b))
a = BFactory()
b = BFactory()
print(id(a), id(b), id(a)==id(b))


# 懒加载, 基于__call__(), metaclass负责维护单实例, 但并发实例化需要保证线程安全
from threading import Lock

class Singleton(type):

    def __init__(self, *args, **kwargs):
        self._instance = None
        self._instance_lock = Lock()
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self._instance:
            return self._instance
        with self._instance_lock:
            if not self._instance:
                self._instance = super().__call__(*args, **kwargs)
            return self._instance

class CFactory(metaclass=Singleton):

    pass


class DFactory(metaclass=Singleton):

    pass


a = CFactory()
b = CFactory()
print(id(a), id(b), id(a)==id(b))
a = DFactory()
b = DFactory()
print(id(a), id(b), id(a)==id(b))


# 懒加载, 基于decorator, 需要为每个类附带一把实例化锁, 在实例化单件成功后可以销毁锁释放空间

from functools import wraps
from threading import Lock
from collections import defaultdict

def singleton(cls):
    _instance = {}
    _instance_lock = defaultdict(Lock)

    def wrapper():
        if cls in _instance:
            return _instance[cls]
        with _instance_lock[cls]:
            if cls not in _instance:
                _instance[cls] = cls()
        del _instance_lock[cls]
        return _instance[cls]

    return wrapper

@singleton
class EFactory:

    pass


@singleton
class FFactory:

    pass


a = EFactory()
b = EFactory()
print(id(a), id(b), id(a)==id(b))
a = FFactory()
b = FFactory()
print(id(a), id(b), id(a)==id(b))
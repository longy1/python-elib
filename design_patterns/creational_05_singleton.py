#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
线程安全的singleton
"""


# 懒加载, 基于类上的__new__(), 接管实例化过程, 需要保证线程安全
from threading import Lock


class Singleton:

    _instance = None
    _instance_lock = Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._instance_lock:
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

    def wrapper(*args, **kwargs):
        if cls in _instance:
            return _instance[cls]
        with _instance_lock[cls]:
            if cls not in _instance:
                _instance[cls] = cls(*args, **kwargs)
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


# 立即加载, 使用类封装一个实例
class GFactory():

    _instance = object()

    def __new__(cls, *args, **kwargs):
        return cls._instance


class HFactory():

    _instance = object()

    def __new__(cls, *args, **kwargs):
        return cls._instance


a = GFactory()
b = GFactory()
print(id(a), id(b), id(a)==id(b))
a = HFactory()
b = HFactory()
print(id(a), id(b), id(a)==id(b))
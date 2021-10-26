#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
线程安全的singleton, 还可以优化全局变量锁
"""
from threading import Lock

singleton_lock = Lock()

class Singleton:

    _instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if cls._instance:
            return cls._instance
        with singleton_lock:
            if not cls._instance:
                cls._instance = super().__new__(cls, *args, **kwargs)
            return cls._instance

a = Singleton()
b = Singleton()
print(id(a), id(b), id(a)==id(b))
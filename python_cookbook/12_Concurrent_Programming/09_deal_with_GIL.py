#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
GIL, Global Interpreter Lock, 意味着一个解释器中只有一个线程能够执行Python字节码
GIL存在原因, GC等机制依赖线程不安全实现的引用计数, 需要锁住以保持线程安全
GIL的影响, 主要影响CPU密集型, 频繁的线程切换却只是等待, 导致多线程不如单线程计算
如何避免GIL的影响
    进行IO密集型任务, 可以几乎无视GIL
    使用多进程或进程池
    使用没有GIL的解释器, 如PyPy
    使用c扩展
总结, 不要乱怪罪GIL, 找到核心的问题
"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
使用concurrent.future库中的ProcessPoolExecutor
只能用进程池加速简单的任务
如果不想主进程被result()阻塞, 可以为其设置异步回调
进程并行只能处理可以被分解为独立部分的问题(但是这部分问题仍然可能存在分支, 是GPU处理不了的)
必须是简单函数形式, 不能支持闭包, 方法
submit()调用的函数和实参, 必须是可以被序列化(兼容pickle)的, 因为涉及进程间通信
任务函数不应该有副作用, 与map reduce的核心思想一致, 要么只有最终结果, 要么出错重做, 不要隐式地做其他事
保持环境简单与纯洁, 不要试图在子进程中修改环境
先创建进程, 再创建线程, 减少进程复制开销
"""

from concurrent.futures import ProcessPoolExecutor
import gzip
import io
import glob


# map-reduce寻找访问了robots.txt的主机

def find_robots(filename):

    robots = set()

    with gzip.open(filename) as f:
        for line in io.TextIOWrapper(f, encoding='ascii'):
            fields = line.split()
            if fields[6] == '/robots.txt':
                robots.add(fields[0])
    return robots

def find_all_robots(logdir):
    files = glob.glob(logdir+'/*.log.gz') # glob实现unix风格的地址匹配
    all_robots = set()
    with ProcessPoolExecutor(5) as executor:
        for robots in executor.map(find_robots, files):
            all_robots.update(robots)
    return all_robots

if __name__ == '__main__':
    robots = find_all_robots('logs')
    for ipaddr in robots:
        print(ipaddr)



#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
使用concurrent.future库中的ThreadPoolExecutor
使用queue库, 手动创建线程池
避免线程无限增长的进程
submit会返回一个标识符t, 通过t.result()可以等待子线程return结果
错误使用result()可能造成循环等待, 进而死锁, 特别地, result自身也会死锁, 类似不可重入锁
"""

# TCP使用线程池示例, 可以用queue实现相同的

from sockt import sockt, AF_INET, SOCK_STREAM
from concurrent.futures import ThreadPoolExecutor

def echo_client(sock, client_addr):
    print(f'Got connenction from {client_addr}')
    whie True:
        msg = sock.recv(65536)
        if not msg:
            break
        sock.sendall(msg)
    print(f'Connection from {client_addr} closed')
    sock.close()

def echo_server(addr):
    pool = ThreadPoolExcutor(10)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        sock, client_addr = sock.accept()
        pool.submit(echo_client, sock, client_addr)

echo_server(('', 15000))


# 官方文档用例

import concurrent.futures
import urllib.request

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']

def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

# 使用with来保证回收资源
with concurrent.futures.ThreadPoolExecutor(5) as executor:
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    for future in future_to_url:
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as e:
            print(f'{url} generated an exception: {e}')
        else:
            print(f'Get {len(data)} bytes from {url}')
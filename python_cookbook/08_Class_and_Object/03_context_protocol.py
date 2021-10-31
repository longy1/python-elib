#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
it needs contextlib.contextmanager or __enter__(), __exit__() for using with on object
"""

from socket import socket, AF_INET, SOCK_STREAM, SHUT_RD
from functools import partial

class LazyConnection:

    def __init__(self, addr, family=AF_INET, con_type=SOCK_STREAM):
        self.addr = addr
        self.family = family
        self.con_type = con_type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.con_type)
        self.sock.connect(self.addr)
        return self.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None

with LazyConnection(('www.python.org', 80)) as conn:
    conn.send(b'GET /index.html HTTP/1.1\r\n')
    conn.send(b'Host: www.python.org\r\n')
    conn.send(b'\r\n')
    res = b''.join(iter(partial(conn.recv, 8192), b'')).replace(b'\r', b'')
    print(res.decode())
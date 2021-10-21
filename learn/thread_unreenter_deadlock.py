#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
hahahahhah
"""

import threading

lock = threading.Lock()

with lock:
    with lock:
        pass

print('end')
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
iter(callable, sentinel), end when callable return sentinel
"""
import sys
import os

with open(os.path.abspath('./13_batch_pipe.py')) as f:
    for chunk in iter(lambda: f.read(10), ''):
        n = sys.stdout.write(chunk)
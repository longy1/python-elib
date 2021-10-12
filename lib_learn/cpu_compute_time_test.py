#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'test time adding i from 0 to n'

__author__ = 'Ethan Long'

import time

n = 2**25
start = time.time()
i = 0
while i < 2**25:
	i += 1
end = time.time()

print(round((end-start), 2))
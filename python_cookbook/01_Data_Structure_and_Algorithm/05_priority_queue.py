#!/usr/bin/ python3
# -*- coding: utf-8 -*-

# how to
import heapq

class PriorityQueue:
	def __init__(self):
		self._queue = []
		self._index = 0

	def push(self, item, priority):
		heapq.heappush(self._queue, (priority, self._index, item))
		self._index += 1

	def pop(self):
		return heapq.heappop(self._queue)

q = PriorityQueue()
q.push('a', 3)
q.push('b', 5)
q.push('c', 2)
q.push('d', 6)
for i in range(4):
	print(q.pop())
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


class Queen(object):

    def __init__(self, degree=8):
        self.degree = degree
        self.status = list(range(degree))
        for i in range(degree):
            self.status[i] = random.randint(0, degree-1)

    def print(self):
        print(self.status)
        print('Conflicts: ', self.get_conflicts(self.status))

    def get_conflicts(self, status):  # 获得当前冲突对数
        conflicts = 0

        for column in range(self.degree):
            for check in range(column + 1, self.degree):
                if status[column] == status[check]:
                    conflicts += 1
                if abs(status[check] - status[column]) == check - column:
                    conflicts += 1
        return conflicts

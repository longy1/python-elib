#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'doc'

__author__ = 'Ethan Long'

class Solution:
    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        # 求标准方程
        # 判断端点是否在线段内(通过点在直线上和点在端点内部), 返回最小的存在端点
        # 斜率相等或都不存在, 则无交点
        # 斜率不相等, 则通过标准方程求唯一交点
        # 交点在两条线段内, 则返回这个唯一交点

        def line_standard_equation_by_point(p1, p2):
            a, b, c, k = None, None, None, None
            x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]

            a = y1-y2
            b = x1-x2
            c = x1*y2 - x2*y1

            k = a / b if b != 0 else float('-inf')

            return a, b, c, k

        def is_equal(f1, f2):
            return abs(f1 - f2) <= 10**(-6)

        def point_in_line(a, b, c, x, y):
            return is_equal(b*y, a*x + c)

        def point_between_2point(p, start, end):
            d = 10**(-6)
            x_min = min(start[0], end[0]) - d
            x_max = max(start[0], end[0]) + d
            y_min = min(start[1], end[1]) - d
            y_max = max(start[1], end[1]) + d
            return x_min <= p[0] <= x_max and y_min <= p[1] <= y_max

        a1, b1, c1, k1 = line_standard_equation_by_point(start1, end1)
        a2, b2, c2, k2 = line_standard_equation_by_point(start2, end2)

        s1 = point_in_line(a2, b2, c2, start1[0], start1[1]) and point_between_2point(start1, start2, end2)
        e1 = point_in_line(a2, b2, c2, end1[0], end1[1]) and point_between_2point(end1, start2, end2)
        s2 = point_in_line(a1, b1, c1, start2[0], start2[1]) and point_between_2point(start2, start1, end1)
        e2 = point_in_line(a1, b1, c1, end2[0], end2[1]) and point_between_2point(end2, start1, end1)

        # print(a1, b1, c1, k1)
        # print(a2, b2, c2, k2)
        # print(s1, e1, s2, e2)
        xy = [float('inf'), float('inf')]
        for i in [(start1, s1), (end1, e1), (start2, s2), (end2, e2)]:
            if i[1]:
                if xy[0] > i[0][0]:
                    xy[0], xy[1] = i[0][0], i[0][1]
                if xy[0] == i[0][0] and xy[1] > i[0][1]:
                    xy[0], xy[1] = i[0][0], i[0][1]
        
        if xy != [float('inf'), float('inf')]:
            return xy

        if k1 == k2 or is_equal(k1, k2):
            return []
        else:
            up, down = b1*c2 - b2*c1, a1*b2 - a2*b1
            x = up / down

            if not is_equal(b1, 0.0):
                y = (a1*x + c1) / b1
            else:
                y = (a2*x + c1) / b2
            
            if point_between_2point([x, y], start1, end1) and point_between_2point([x, y], start2, end2):
                return [x, y]
            
            return []
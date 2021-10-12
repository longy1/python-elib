#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'count two player\'s winable position'

__author__ = 'Ethan Long'

class Solution:
    def tictactoe(self, board: List[str]) -> str:
        # 对每一个玩家:
        # 求其可能赢的行, 列, 对角线
        # 对于每一种能赢的情况, 为该情况上的空格+1计数
        # 玩家轮流填自己计数最大的非空位置, 填满之后一定有一个玩家获胜

        from collections import defaultdict
        do = defaultdict(int)
        dx = defaultdict(int)

        def fill(board, point, char):
            board[point[0]][point[1]] = char

        # 遍历行, 同时记录列
        o_can = [True] * len(board)
        x_can = [True] * len(board)
        co, cx = 0, 0
        for k, v in enumerate(board):
            co = v.count('O')
            cx = v.count('X')
            if co == len(board):
                return 'O'
            if cx == len(board):
                return 'X'

            if co or cx:
                for i in range(len(v)):
                    if v[i] == ' ':
                        if not co:
                            dx[(k, i)] += 1
                        if not cx:
                            do[(k, i)] += 1
                    if v[i] == 'O':
                        x_can[i] = False
                    if v[i] == 'X':
                        o_can[i] = False
        # print(do, dx)
        # print(o_can, x_can)
        for i in range(len(board)):
            if o_can[i] or x_can[i]:
                co, cx = 0, 0
                for j in range(len(board)):
                    if board[j][i] == 'X':
                        cx += 1
                    if board[j][i] == 'O':
                        co += 1
                    if board[j][i] == ' ':
                        if o_can[i]:
                            do[(j, i)] += 1
                        if x_can[i]:
                            if (j, i) == (0, 2):
                                print(1)
                            dx[(j, i)] += 1

                if co == len(board):
                    return 'O'
                if cx == len(board):
                    return 'X'
        # print(do, dx)
        # 对角线
        lco, lcx = 0, 0
        rco, rcx = 0, 0
        blank = []
        rblank = []
        for i in range(len(board)):
            x, y = i, len(board) - 1 - i
            if board[i][i] == 'O':
                lco += 1
            if board[i][i] == 'X':
                lcx += 1
            if board[i][i] == ' ':
                blank.append((i, i))
            if board[x][y] == 'O':
                rco += 1
            if board[x][y] == 'X':
                rcx += 1
            if board[x][y] == ' ' and i != y:
                rblank.append((x, y))
        # print(lco, lcx, rco, rcx, blank, rblank)
        for p in blank:
            if not lco:
                dx[p] += 1
            if not lcx:
                do[p] += 1
        for p in rblank:
            if not rco:
                dx[p] += 1
            if not rcx:
                do[p] += 1

    print(do, dx)
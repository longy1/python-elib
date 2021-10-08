#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a solution of N-Queens problem'

__author__ = 'Ethan Long'

n = 8

def solve_n_queens(n):
    ret = []
    dfs([], 0, list(range(n)), ret, n)

    sol = []
    for res in ret:
        n_sol = []
        for k, v in enumerate(res):
            n_sol.append('.'*res[k] + 'Q' + '.'*(n-res[k]-1))
        sol.append(n_sol)
    return sol


def dfs(path, c_row, a_col, ret, n):
    if len(path) == n:
        ret.append(path)
        return

    if len(a_col) == 0:
        return

    for i in range(len(a_col)):
        if not if_conflict(path, c_row, a_col[i], n):
            dfs(path+[a_col[i]], c_row+1, a_col[0:i]+a_col[i+1:], ret, n)

def if_conflict(path, row, col, n):
    i, j, k = row-1, col-1, col+1
    while i >= 0:
        if j >= 0:
            if path[i] == j:
                return True
        if k < n:
            if path[i] == k:
                return True
        i, j, k = i-1, j-1, k+1
    return False

sol = solve_n_queens(n)
print(sol)
print(len(sol))
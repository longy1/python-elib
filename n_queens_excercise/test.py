#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from queen import Queen
from hill_climbing import hill_climbing
from simulated_annealing import simulated_annealing
from genetic_algorithms import genetic_algorithms

# 需求解N皇后问题, 修改degree即可
degree = 8
print('求解5个随机{}皇后问题：'.format(degree))
for i in range(5):
    # 随机生成测试数据
    test = Queen(degree)
    print('Test {}: {}'.format(i, test.status))

    # 最陡上升爬山法求解, 传入任意Queen()实例. 成功则返回目标status列表与cost值组成的tuple, 失败时返回的status列表为空.
    hill_climbing_solve = hill_climbing(test)
    if len(hill_climbing_solve[0]) > 0:
        print('最陡上升爬山法得到解: {}, 代价: {}'.format(hill_climbing_solve[0], hill_climbing_solve[1]))
    else:
        print('使用爬山法求解失败: 本次求解仅可得到局部最优解.')

    # 模拟退火算法求解, 传入任意Queen()实例与温度函数的底数. 返回目标status列表与cost值组成的tuple, 失败时返回的status列表为空.
    simulated_annealing_solve = simulated_annealing(test, base=0.99)
    if len(simulated_annealing_solve[0]) > 0:
        print('模拟退火算法得到解: {}, 代价: {}'.format(simulated_annealing_solve[0], simulated_annealing_solve[1]))
    else:
        print('本次模拟退火算法求解失败, 温度为0时仍未得到解.')

    # 遗传算法求解, 传入棋盘边长, 种群容量, 变异概率, 最大繁衍代数. 成功则返回目标status列表与cost值组成的tuple, 失败时返回的status列表为空.
    genetic_algorithms_solve = genetic_algorithms(degree=degree, p_num=30, mutate_rate=0.6, generation=200)
    if len(genetic_algorithms_solve[0]) > 0:
        print('遗传算法得到解: {}, 代价: {}'.format(genetic_algorithms_solve[0], genetic_algorithms_solve[1]))
    else:
        print('本次遗传算法求解失败: 超过最大繁衍代数.')

    print('')

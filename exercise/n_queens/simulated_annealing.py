import random
import math


def simulated_annealing(queen, base=0.99):
    cost = 0
    time = 1  # 时间递增变量
    status = list(queen.status)  # 当前状态

    while time > 0:
        # 更新温度
        cost += 1
        time += 1
        temprature = schedule(time, queen, base)

        # 到达目标状态时返回目标解
        if queen.get_conflicts(status) == 0:
            return status, cost
        # 温度为0且未达到目标状态时, 返回空解
        elif temprature == 0:
            return [], cost
        # 随机拓展下一个状态
        next_status = list(status)
        row = random.randint(0, queen.degree-1)
        column = random.randint(0, queen.degree-1)
        next_status[column] = row
        # 评估拓展状态, 更新当前状态
        delta = queen.get_conflicts(status) - queen.get_conflicts(next_status)
        if delta >= 0:
            status = next_status
        else:
            if math.exp(delta / temprature) > random.random():
                status = next_status


def schedule(time, queen, base):
    return queen.degree * queen.degree * pow(base, time)

import random


# 传入Queen的实例, 使用爬山法求其解, 成功则返回解list, 失败返回空list
def hill_climbing(queen):
    cost = 0
    lateral = 0  # 横移次数
    status = queen.status  # 当前状态
    conflicts = queen.get_conflicts(status)  # 当前冲突对数

    while conflicts >= 0:
        cost += 1
        last_conflicts = conflicts

        next_moves = []  # 使conflicts最小的next_status集合
        min_conflicts = queen.get_conflicts(status)  # 保存最优解集合对应的最小conflics, 初始化为当前conflicts
        if min_conflicts == 0:
            return queen.status, 0

        # 遍历计算任意移动一次皇后之后的conflicts, 得到最佳邻接结点集合
        for row in range(queen.degree):
            for column in range(queen.degree):
                next_status = list(status)
                next_status[column] = row
                next_conflicts = queen.get_conflicts(next_status)

                if next_conflicts == min_conflicts:  # 遇到相等时加入最佳邻接结点集合
                    if next_status not in next_moves:
                        next_moves.append(list(next_status))
                if next_conflicts < min_conflicts:  # 遇到更好的最佳邻接结点时, 清空原集合并更新最优解
                    next_moves.clear()
                    next_moves.append(list(next_status))
                    min_conflicts = next_conflicts

        # 在最佳邻接结点中随机选取一项作为当前结点, 同时更新当前conflicts, 若最佳邻接结点比当前结点都要差, 将conflicts置为-1
        if len(next_moves) == 0 and next_moves[0] == status:
            conflicts = -1
        else:
            status = next_moves[0] if len(next_moves) == 1 else next_moves[random.randint(0, len(next_moves) - 1)]
            conflicts = min_conflicts

        # 判断爬山前后冲突对数是否改变, 并更新横向移动次数
        lateral = lateral + 1 if last_conflicts == conflicts else 0

        # 无冲突对时得到全局最优解, 返回目标状态
        if conflicts == 0:
            return status, cost
        # 无法移动或反复横移超过阈值时得到局部最优解, 返回空
        if conflicts == -1 or lateral == 100:
            return [], cost

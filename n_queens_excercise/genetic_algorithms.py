import random
from queen import Queen


def genetic_algorithms(degree=8, p_num=50, mutate_rate=0.6, generation=500):
    population = []  # 种群, 包含所有基因
    target_fit = -1
    # 生成初始基因群
    for i in range(p_num):
        queen = Queen(degree=degree)
        population.append(queen)

    cost = 0
    for i in population:
        if fitness_func(i) == target_fit:
            return i.status, cost * p_num
    # 繁衍循环, 发现适合基因或代价超过上限时结束循环
    while cost < generation:
        cost += 1
        next_population = []
        # 根据适应度随机选取繁衍对, 按一定概率突变并产生下一代
        for i in range(len(population)):
            x = random_select(population, fitness_func)
            y = random_select(population, fitness_func)
            child = reproduce(x, y)
            # 以突变率发生突变
            if random.random() < mutate_rate:
                mutate(child)
            next_population.append(child)
        population = next_population
        # 遍历获取种群适应度, 得到适应序列
        for i in population:
            if fitness_func(i) == target_fit:
                return i.status, cost * p_num
    # 未寻找到合适个体时返回空解
    return [], cost * p_num


def fitness_func(gene):
    conflicts = gene.get_conflicts(gene.status)
    return -1 if conflicts == 0 else 1 / conflicts


def random_select(population, fitfunc):
    fitness = []
    full = 0
    for i in population:
        fitness.append(fitfunc(i))
        full += fitness[-1]
    rand = random.random() * full
    for i, value in enumerate(fitness):
        rand -= value
        if rand <= 0:
            return population[i]


def reproduce(x, y):
    child = Queen(degree=x.degree)
    p_break = random.randint(0, len(x.status) - 1)
    child.status = list(x.status[0:p_break] + y.status[p_break:len(y.status)])
    return child


def mutate(child):
    child.status[random.randint(0, child.degree-1)] = random.randint(0, child.degree-1)


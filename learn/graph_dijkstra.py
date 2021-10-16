#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a stupid Dijkstra Algorithm'

__author__ = 'Ethan Long'

from collections import defaultdict

# nodes, set of nodes, [Node1, Node2]
# c, method to compute cost(u, v), [(Node1, Node2, cost)]
def Dijkstra(m, nodes):
    visit_nodes = ['u']
    d = defaultdict() # d[nodes] = [distance, last_node]

    for i in nodes:
        if i != 'u':
            cost = get_cost('u', i, m)
            d[i] = [cost, 'u']

    while set(visit_nodes) != set(nodes):
        diff = [x for x in nodes if x not in visit_nodes and x in d and x != 'u']
        diff = [[d[x][0], x] for x in diff]
        diff.sort()
        next_node = diff[0][1]
        visit_nodes.append(next_node)

        next_neighbors = get_neighbor(next_node, m)
        next_neighbors = [x for x in next_neighbors if x not in visit_nodes]
        for n in next_neighbors:
            cost = d[next_node][0] + get_cost(next_node, n, m)
            if cost < d[n][0]:
                d[n] = [cost, next_node]
    return d

def get_neighbor(node, m):
    neighbor = set()
    for i in m:
        if node in i:
            if node == i[0]:
                neighbor.add(i[1])
            else:
                neighbor.add(i[0])
    return list(neighbor)

def get_cost(node1, node2, m):
    for i in m:
        if node1 in i and node2 in i:
            return i[2]
    return float('inf')

m = [('u', 'x', 1), ('u', 'v', 2), ('u', 'w', 5), ('v', 'x', 2), ('v', 'w', 3),
     ('x', 'w', 3), ('y', 'x', 1), ('w', 'y', 1), ('w', 'z', 5), ('y', 'z', 2),]
n = ['x', 'y', 'z', 'u', 'v', 'w']

# print(get_cost('u', 'v', m))
# print(get_neighbor('u', m))
d = Dijkstra(m, n)
print(d)
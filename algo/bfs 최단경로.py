# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 16:11:34 2019

@author: kjh1
"""
graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E','G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}


def bfs(graph, start_node):
    visit = {}
    queue = list()
    queue.append(start_node)
    
    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit[node] = True
            queue.extend(graph[node])

    return visit

print(list(bfs(graph,'A').keys()))
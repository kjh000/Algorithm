# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:26:18 2019

@author: kjh1
"""

#graph = {
#    'A': ['B'],
#    'B': ['A', 'C', 'H'],
#    'C': ['B', 'D'],
#    'D': ['C', 'E','G'],
#    'E': ['D', 'F'],
#    'F': ['E'],
#    'G': ['D'],
#    'H': ['B', 'I', 'J', 'M'],
#    'I': ['H'],
#    'J': ['H', 'K'],
#    'K': ['J', 'L'],
#    'L': ['K'],
#    'M': ['H']
#}

graph = {
    'A': ['B','C'],
    'B': ['A', 'D'],
    'C': ['A','E','F'],
    'D': ['B', 'H','I'],
    'E': ['C'],
    'F': ['C','G'],
    'G': ['F'],
    'H': ['D'],
    'I': ['D']
    
}


def dfs(graph, start_node):
    
    visit = {}
    stack = list()

    stack.append(start_node)

    while stack: 
        node = stack.pop()
        if node not in visit:
            visit[node] = True
            stack.extend(graph[node])
            
    return visit


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

dfs_ouput = list(dfs(graph,'A').keys())
#print(list(dfs(graph,'A').keys()))
#print(list(bfs(graph,'A').keys()))
print(dfs_ouput)

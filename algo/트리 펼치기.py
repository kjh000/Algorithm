# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 12:45:35 2019

@author: kjh1
"""


graph = {
    'A': ['B','C'],
    'B': ['A', 'D'],
    'C': ['A','E','F'],
    'D': ['B','H','I'],
    'E': ['C'],
    'F': ['C','G'],
    'G': ['F'],
    'H': ['D'],
    'I': ['D']
    
}


graph_parent = {
    'A': -1,
    'B': 'A',
    'C': 'A',
    'D': 'B',
    'E': 'C',
    'F': 'C',
    'G': 'F',
    'H': 'D',
    'I': 'D'
    
}


graph_weight = {
    'A': [1,0,2],
    'B': [1,0,1],
    'C': [1,0,2],
    'D': [1,0,2],
    'E': [1,0,0],
    'F': [1,0,1],
    'G': [1,0,0],
    'H': [1,0,0],
    'I': [1,0,0]
    
}

lenth = [0]*(len(graph))
mat = []

def dfs(graph, start_node):
    i = 0
    visit = {}
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit[node] = True
            stack.extend(graph[node])
            i += 1
    return visit


dfs_ouput = list(dfs(graph,'A').keys())
print(dfs_ouput)

for i in range(9):
    lenth[i] = len(graph[dfs_ouput[i]])
    
print(lenth)

queue = []
for i in graph:

    if(len(graph[i]) == 1):
        
        queue.append(i)
#        graph_weight[i][1] += 1
        
while queue:

    node = queue.pop()        
    parent = graph_parent[node]
    if(parent == -1): break
    
    if(graph_weight[parent][1] < graph_weight[parent][2]):
        graph_weight[parent][0] += graph_weight[node][0]
        graph_weight[parent][1] += 1
        
    
    if(graph_weight[parent][1] == graph_weight[parent][2]):
        queue.append(parent)
    
    
    
print(graph_weight)
    
    
    
    
    
    
    
    
    
    
    
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:43:12 2019

@author: kjh1
"""


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


ordering = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'E': 0,
    'F': 0,
    'G': 0,
    'H': 0,
    'I': 0
    
}

visited = {
    'A': False,
    'B': False,
    'C': False,
    'D': False,
    'E': False,
    'F': False,
    'G': False,
    'H': False,
    'I': False
    
}
affects = {
    'A': False,
    'B': False,
    'C': False,
    'D': False,
    'E': False,
    'F': False,
    'G': False,
    'H': False,
    'I': False
    
}

idx = 1
def dfs(u):
    global idx
    l = idx
    visited[u] = True
    ordering[u] = idx
    
    for i in graph[u]:
        if(visited[i] == False):
            idx += 1
            dfs(i)
    r = idx
    affects[u] = [l,r]
    
    
dfs('A')
print(ordering)
print(affects)    


#dfs_ouput = list(dfs(graph,'A').keys())


# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 12:16:39 2019

@author: kjh1
"""
import sys


def dijkstra(K,V,graph):
    
    INF = sys.maxsize
    
    s =[False]*V
    
    d = [INF]*V 

    d[K-1] = 0    
    
    while True:
        
        m = INF
        N = -1
        
        for j in range(V):
            if not s[j] and m >d[j]:
                m = d[j]
                N = j
                
                
        if m == INF:
            break
        
        s[N] = True
        
        
        for j in range(V):
            
            if s[j]: continue
            via = d[N] + graph[N][j]
            
            if d[j]>via:
                d[j] = via
                
    return d

V,E,x = map(int,input().split())
mat = []
re_mat = []

INF = sys.maxsize
graph = [[INF]*V for _ in range(V)]
re_graph = [[INF]*V for _ in range(V)]

for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u-1][v-1] = w
    re_graph[v-1][u-1] = w
for d in dijkstra(x,V,graph):
#    print(d if d!= INF else 'INF')
    mat.append(d)

for d in dijkstra(x,V,re_graph):
#    print(d if d!= INF else 'INF')
    re_mat.append(d)    
    
for i in range(V):
    mat[i] = mat[i] + re_mat[i]
    
#print(mat)
print(max(mat))
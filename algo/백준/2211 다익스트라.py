# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 12:20:55 2020

@author: kjh1
"""
import sys

def dijkstra(V,graph):
    
    INF = sys.maxsize
    
    s =[False]*V
    
    d = [INF]*V 

    d[0] = 0
    
    line = [0]*V
    
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
                line[j] = N
#                
                
                
    return line

V,E = map(int,input().split())
K = 1
INF = sys.maxsize
graph = [[INF]*V for _ in range(V)]


for _ in range(E):
    u,v,w = map(int,input().split())
    
    graph[u-1][v-1] = w
    graph[v-1][u-1] = w 
    
line = dijkstra(V,graph)
#print(dijkstra(V,graph))


print(V-1)
for i in range(1,V):
    print(i+1,line[i]+1)    
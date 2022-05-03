# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 17:34:50 2019

@author: kjh1
"""
import sys


T = int(input())

for t in range(T):
    
    n,m = map(int,input().split())
    
    
    graph = [[2]*n for _ in range(n)]
    
    edges = n*(n-1)//2
    vertices = n
    ans = 0
    
    
    
    for i in range(m):
#        u, v = map(int,input().split())
        u,v = map(int,sys.stdin.readline().split())
        
        
        graph[u-1][v-1] = 1
        graph[v-1][u-1] = 1
    
    
    
    
    T = set()
    X = set()
    
    X.add(0)
    
    
    while len(X) != vertices:
        crossing = set()
        for x in X:
            for k in range(vertices):
                if k not in X and graph[x][k] != 0:
                    crossing.add((x, k,graph[x][k]))
        edge = sorted(crossing, key=lambda e:graph[e[0]][e[1]])[0]
        T.add(edge)
        X.add(edge[1])
        
    T = list(T)    
    
    for i in range(len(T)):
    
        ans += T[i][2]
        
    print("Case #{}: {}".format(t+1,ans))
        
    

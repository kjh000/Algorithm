# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 11:58:42 2019

@author: kjh1
"""
import sys

T = int(input())

for t in range(T):
    
    n,m = map(int,input().split())
    
    
    match = [-1]*(n+1)
    
    v = {}
    ans = 0
    
    
    def dfs(here):
        
        if visited[here] != 0:
            return 0
        
        visited[here] = 1
        
        for i in range(len(v[here])):
            work = v[here][i]
            if(match[work] == -1 or dfs(match[work]) != 0):
                match[work] = here
                return 1
        
        return 0
    
            
    
    for i in range(m):
        v[i+1] = []
        
    for i in range(m):
        a,b = map(int,input().split())        
        
        for j in range(b-a+1):
            v[i+1].append(a+j)
            
    for i in range(m):
        visited = [0]*(m+1)
        
        ans += dfs(i+1)
        
    print(ans)


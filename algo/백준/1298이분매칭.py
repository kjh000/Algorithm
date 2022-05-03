# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 11:58:42 2019

@author: kjh1
"""
import sys
n,m = map(int,input().split())


match = [-1]*(5001)

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

        
for i in range(n):
    v[i+1] = []
    
for i in range(m):
    a,b = map(int,input().split())
    v[a].append(b)
        
        

for i in range(n):
    visited = [0]*(1001)
    
    if dfs(i+1):
        ans += 1
    
print(ans)

"""
visit = [0]*(n+1)  ---> error

visit = [0]*(1001) ---> ok

why?????

"""
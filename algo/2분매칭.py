# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 11:58:42 2019

@author: kjh1
"""
import sys
n,m = map(int,input().split())
"""
n = people, m = tasks
"""

match = [-1]*(m+1)

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
    l = list(map(int,input().split()))
#    l = list(map(int,sys.stdin.readline().split()))
    
    v[i + 1] = []
    
    for j in range(l[0]):
        v[i+1].append(l[j+1])
        
for i in range(n):
    visited = [0]*(n+1)
    
    ans += dfs(i+1)
    
print(ans)


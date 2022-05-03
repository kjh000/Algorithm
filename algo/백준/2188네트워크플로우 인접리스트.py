# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:39:34 2019

@author: kjh1
"""
import sys
n,m = map(int,input().split())

MAX = n+m+2
INF = 10**9 + 1
edges = {}

capacity = [[0]*MAX for _ in range(MAX)]
flow = [[0]*MAX for _ in range(MAX)]


for i in range(n+m+2):
    edges[i] = []
    

for i in range(n):
    edges[0].append(i+1)
    edges[i+1].append(0)
for i in range(m):
    edges[n+m+1].append(i+n+1)
    edges[i+n+1].append(n+m+1)

def maxFlow(start,end):
    
    result = 0
    while(1):
        visit = [-1]*MAX
        q = []
        q.append(start)
        
        while q:
            x = q.pop( )
            
            for i in range(len(edges[x])):
                
                y = edges[x][i]
                if(capacity[x][y] - flow[x][y] > 0 and visit[y] == -1):
                    q.append(y)
                    visit[y] = x
                    if(y == end): break
                
    
        if(visit[end] == -1): break
    
        tmp_flow = INF
        cur = end
        while cur != start:
            tmp_flow = min(tmp_flow,capacity[visit[cur]][cur] - flow[visit[cur]][cur])
            cur = visit[cur]
            
        cur = end
        while cur != start:
            flow[visit[cur]][cur] += tmp_flow
            flow[cur][visit[cur]] -= tmp_flow
            
            cur = visit[cur]
            
            
        result += tmp_flow
        
    return result

for i in range(n):
    
    l = list(map(int,input().split()))
#    l = list(map(int,sys.stdin.readline().split()))
    
    for j in range(l[0]):
        
        edges[i+1].append(l[j+1]+n)
        edges[l[j+1]+n].append(i+1)
        capacity[i+1][l[j+1]+n] = 1
    
    capacity[0][i+1] = 1
    
    
for i in range(m):
    
    capacity[i+n+1][-1] = 1

print(maxFlow(0,n+m+1))


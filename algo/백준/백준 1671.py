# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:13:04 2019

@author: kjh1
"""
n = int(input())

INF = 10**9 + 1
MAX = 2*n+2


capacity = [[0]*MAX for _ in range(MAX)]
flow = [[0]*MAX for _ in range(MAX)]

edges = {}

mat = [list(map(int,input().split())) for _ in range(n)]

for i in range(MAX):
    edges[i] = []
    
for i in range(n):
    edges[0].append(i+1)
    edges[i+1].append(0)
    capacity[0][i+1] = 2
    
    edges[MAX-1].append(i+n+1)
    edges[i+n+1].append(MAX-1)
    capacity[i+n+1][MAX-1] = 1
    
    

for i in range(n):
    for j in range(n):
        if(i == j):
            continue
        
        if(mat[i][0] == mat[j][0] and mat[i][1] == mat[j][1] and mat[i][2] == mat[j][2]):
            
            if(i>j):
                continue
            
            edges[i+1].append(j+1+n)
            edges[j+1+n].append(i+1)
            capacity[i+1][j+1+n] = 1
            
            
        elif(mat[i][0] >= mat[j][0] and mat[i][1] >= mat[j][1] and mat[i][2] >= mat[j][2]):
            edges[i+1].append(j+1+n)
            edges[j+1+n].append(i+1)
            capacity[i+1][j+1+n] = 1
            
        
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

a = maxFlow(0,MAX-1)
print(n-a)

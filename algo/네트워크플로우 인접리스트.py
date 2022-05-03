# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 15:42:43 2019

@author: kjh1
"""

MAX = 100
## MAX = total node
INF = 10**9 + 1

n = 6
#n = int(input())

capacity = [[0]*MAX for _ in range(MAX)]
flow = [[0]*MAX for _ in range(MAX)]

edges = {}

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
    edges[i+1] = []
    

    
for i in range(10):
    
    s,e,f = map(int,input().split())
    edges[s].append(e)
    edges[e].append(s)
    capacity[s][e] = f
    


a = maxFlow(1,6)
print(a)














# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:18:49 2019

@author: kjh1
"""
import sys
INF = 10**9 + 1

c = int(input())
for C in range(c):
    # source : 0 , player : 1~11 , position : 12~22 , sink : 23
    start,end = 0,23
    
    capacity = [[0]*24 for _ in range(24)]
    flow = [[0]*24 for _ in range(24)]
    weight = [[0]*24 for _ in range(24)]
    
    mat = [list(map(int,input().split())) for _ in range(11)]
#    mat = [list(map(int,sys.stdin.readline().split())) for _ in range(11)]
    adj = {}
    ans = 0
    
    for i in range(24):
        adj[i] = []
        
        
    for i in range(11):
        adj[0].append(i+1)
        adj[23].append(i+12)
        
        adj[i+1].append(0)
        adj[i+12].append(23)
        
        capacity[0][i+1] = 1
        capacity[i+12][23] = 1
        
    for i in range(11):
        for j in range(11):
            if(mat[i][j] != 0):
                adj[i+1].append(j+12)
                adj[j+12].append(i+1)
                capacity[i+1][j+12] = 1
                weight[i+1][j+12] = -mat[i][j]
                weight[j+12][i+1] = mat[i][j]
                
    
        
        
    
    result = 0
    
    while 1:
        visit = [-1]*24
        dist = [INF]*24
        inQ = [False]*(24)
        
        dist[start] = 0
        inQ[start] = True
        
        q = []
        q.append(start)
        
    
            
        while q:
            x = q.pop( )
            inQ[x] = False
            
            for i in range(len(adj[x])):
            
                y = adj[x][i]
                if(capacity[x][y] - flow[x][y] > 0 and dist[y] > dist[x] + weight[x][y]):
                    
                    visit[y] = x
                    dist[y] = dist[x] + weight[x][y]
                    if(inQ[y] == False):
                        
                        q.append(y)
                        inQ[y] = True
    #                if(y == end): break
    
                
        if(visit[end] == -1):
            break
        
        
    #    tmp_flow = INF
        
        tmp_flow = 1
        cur = end
    #    
        while cur != start:
    
            tmp_flow = min(tmp_flow,capacity[visit[cur]][cur] - flow[visit[cur]][cur])
            cur = visit[cur]
            
        cur = end
        
    #    print('tmp_flow : {}'.format(tmp_flow))
        while cur != start:
            
            flow[visit[cur]][cur] += tmp_flow
            flow[cur][visit[cur]] -= tmp_flow
            
            result += weight[visit[cur]][cur]*(tmp_flow)
    
            
            cur = visit[cur]
                
        
    print(-result)



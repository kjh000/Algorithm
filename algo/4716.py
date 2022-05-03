# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 10:30:54 2019

@author: kjh1
"""
INF = 10**9 + 1

n,a,b = map(int,input().split())

MAX_NODE = n+4
start = 0
ra = 1
rb = 2
end = MAX_NODE-1
result = 0
adj = {}

#i,cfw
for i in range(MAX_NODE):
    adj[i] = []

adj[0].append([1,a,0,0])
adj[0].append([2,b,0,0])
adj[1].append([0,0,0,0])
adj[2].append([0,0,0,0])


for i in range(1,n+1):
    adj[1].append([i+2,0,0,0])
    adj[i+2].append([1,0,0,0])
    
    adj[2].append([i+2,0,0,0])
    adj[i+2].append([2,0,0,0])
    
    adj[end].append([i+2,0,0,0])
    adj[i+2].append([end,0,0,0])

#a,b,end
#0,3~

for i in range(1,n+1):
    
    k,da,db = map(int,input().split())
    
    
    adj[1][i][1] = k
    adj[i+2][0][3] = -da
    
    adj[2][i][1] = k
    adj[i+2][1][3] = -db
    
    adj[i+2][2][1] = k
    
    adj[1][i][3] = da
    adj[2][i][3] = da
    


    
while 1:
    visit = [-1]*MAX_NODE
    dist = [INF]*MAX_NODE
    inQ = [False]*(MAX_NODE)
    
    dist[start] = 0
    inQ[start] = True
    
    q = []
    q.append(start)
    

        
    while q:
        x = q.pop( )
        inQ[x] = False
        
        for i in range(len(adj[x])):
        
            y = adj[x][i][0]
            if(adj[x][i][1] - adj[x][i][2] > 0 and dist[y] > dist[x] + adj[x][i][2]):
                
                visit[y] = x
                dist[y] = dist[x] + adj[x][i][2]
                if(inQ[y] == False):
                    
                    q.append(y)
                    inQ[y] = True
#                if(y == end): break

            
    if(visit[end] == -1):
        break
    
    
    tmp_flow = INF
    
#    tmp_flow = 1
    cur = end
    
    while cur != start:

        tmp_flow = min(tmp_flow,adj[visit[cur]][cur][1] - adj[visit[cur]][cur][2])
        cur = visit[cur]
        
    cur = end
    
    while cur != start:
        
        adj[visit[cur]][cur][2] += tmp_flow
        adj[cur][visit[cur]][2] -= tmp_flow
        
        result += adj[visit[cur]][cur][3]*(tmp_flow)

        
        cur = visit[cur]

print(result)

    
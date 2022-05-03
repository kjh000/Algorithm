# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:49:39 2019

@author: kjh1
"""
import sys

n,k,m = map(int,input().split())


graph = {}
queue = list()
distance = [-1]*(n+m+1)
distance[1] = 0

l = 1

for i in range(1,n+m+1):
    graph[i] = []

for i in range(m):
    
#    h = list(map(int,input().split()))
    
    h = list(map(int,sys.stdin.readline().split()))
    
    
    for j in range(k):
        
        graph[i+1+n].append(h[j])
        graph[h[j]].append(i+n+1)
        

queue.append(1)

while queue:
    
    node = queue.pop(0)
    
    for i in range(len(graph[node])):
        if(distance[graph[node][i]] == -1):
            queue.append(graph[node][i])
            distance[graph[node][i]] = distance[node] + 1
            
            if(graph[node][i] == n):
                l = 0
                break
    
    if(l == 0):
        break



if(distance[n] == -1):
    print(-1)
else:

    print(distance[n]//2 +1)

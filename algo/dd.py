# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:46:26 2019

@author: kjh1
"""
import queue as Q

 
n, m = map(int, input().split())
DIST = [1e9]*(n+1)
start = 1
D = [[] for i in range(n+1)]
inqueue = [False]*(n+1)
 
def SPFA(src):
 
    q = list()
    q.append(src)
    DIST[src]=0
    
 
    while q:
        here = q[0]
        q.remove(q[0])
        
        inqueue[here]=True
        
 
        length = len(D[here])
        for i in range (length):
            cost = DIST[here] + D[here][i][1]
            Next = D[here][i][0]
            if DIST[Next] > cost:
                DIST[Next] = cost
                if inqueue[Next] is False:
                    q.append(Next)
                    inqueue[Next] = True
        
#        if q:
#            if(DIST[q[-1]] < DIST[q[0]]):
#                u = q.pop()
#                q.insert(0,u)

    for i in range(1, n+1):
        if DIST[i] is 1e9:
            print("INF")
        else:
            print(DIST[i])
            
    print(inqueue)
 
while m:
    m -= 1
    a, b, c = map(int, input().split())
    D[a].append((b, -c))
 
SPFA(start)

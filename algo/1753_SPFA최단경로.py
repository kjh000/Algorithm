# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:46:26 2019

@author: kjh1
"""
import queue as Q

 
v, e = map(int, input().split())
DIST = [1e9]*(v+1)
start = int(input())
adj = [[] for i in range(v+1)]
inqueue = [False]*(v+1)
 
#def SPFA(src):
# 
##    q = Q.Queue()
#    q = list()
##    q.put(src)
#    q.append(src)
#    DIST[src]=0
# 
#    while not q.empty():
#        here = q.get()
#        inqueue[here]=False
#        
# 
#        length = len(adj[here])
#        for i in range (length):
#            cost = DIST[here] + adj[here][i][1]
#            Next = adj[here][i][0]
#            if DIST[Next] > cost:
#                DIST[Next] = cost
#                if inqueue[Next] is False:
#                    q.put(Next)
#                    inqueue[Next] = True
#                    
 
def SPFA(src):
 
    q = list()
    q.append(src)
    DIST[src]=0
    
 
    while q:
        here = q[0]
        q.remove(q[0])
#        inqueue[here]=False
        
        inqueue[here]=True
        
 
        length = len(adj[here])
        for i in range (length):
            cost = DIST[here] + adj[here][i][1]
            Next = adj[here][i][0]
            if DIST[Next] > cost:
                DIST[Next] = cost
                if inqueue[Next] is False:
                    q.append(Next)
                    inqueue[Next] = True
        
#        if q:
#            if(DIST[q[-1]] < DIST[q[0]]):
#                u = q.pop()
#                q.insert(0,u)

    for i in range(1, v+1):
        if DIST[i] is 1e9:
            print("INF")
        else:
            print(DIST[i])
            
    print(inqueue)
 
while e:
    e -= 1
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
 
SPFA(start)
# 
#for i in range(1, v+1):
#    if DIST[i] is 1e9:
#        print("INF")
#    else:
#        print(DIST[i])


# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 14:11:21 2019

@author: kjh1
"""
import sys

T = int(input())

for t in range(T):

    v,e = map(int,input().split())
    
    graph = {}
    bd = 0
    coin = 1
    
    for i in range(v):
        graph[i+1] = []
    
    
    
    
    for i in range(e):
        
        a,b = map(int,sys.stdin.readline().split())
        
#        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    
    
    visit = {}
    stack = list()
    
    for i in range(v):
        
        check = [0]*(v+1)
        if(i+1 in visit):
            pass
        else:
            
            stack.append(i+1)
            
            while stack:
                node = stack.pop()
                
                
                if node not in visit:
                    visit[node] = True
                    stack.extend(graph[node])
                    
        #        print(node,coin)
                
                if(check[node] == 0):
                    check[node] = coin
                else:
                    if(check[node] != coin):
        #                print('check! {} {}'.format(node,coin))
                        bd = 1
                
                coin = -coin
        
            stack.clear()
            
            check = [0]*(v+1)
    
#    print(check)
#    print(bd)
    if(bd == 0):
        print('YES')
    else:
        print('NO')
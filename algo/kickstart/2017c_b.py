# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 13:30:01 2019

@author: kjh1
"""

T= int(input())

for t in range(T):
    
    N = int(input())
    
    state = 'POSSIBLE'
    
    cnt = 0
    
    check = -1
    cnt1 = 0
    
    
    grids =[[None]*N for i in range(N)]
    
    
    for i in range(N):
        grids[i] = input()
        if(grids[i].count('X') == 1):
            check = i
        
    for i in range(N):
        if(grids[i].count('X') >= 3):
            state = 'IMPOSSIBLE'
    
        
    for i in range(N):
        for j in range(N):
            if(grids[j][i] == 'X'):
                cnt += 1
                
        if(cnt >= 3):
            state = 'IMPOSSIBLE'
        cnt = 0
        
    if(check>=0):
        for i in range(N):
            if(grids[i][grids[check].index('X')] == 'X'):
                cnt1 += 1
                
            if(cnt1 >= 2):
                state = 'IMPOSSIBLE'
        
        
        
        
    print('Case #{}: {}'.format(t+1,state))
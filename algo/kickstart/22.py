# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 15:35:50 2019

@author: kjh1
"""

T = int(input())

for t in range(T):
    N = int(input())
    
    score = list(map(int,input()))
    
    if(N%2 == 0):
        a = N//2
    else:
        a = (N//2)+1
        
    
    total = sum(score[:a])
    
    for i in range(1,N-a+1):
        if(sum(score[i:i+a])>=total):
            total = sum(score[i:i+a])
    
    
    print('Case #{}: {}'.format(t+1,total))
          
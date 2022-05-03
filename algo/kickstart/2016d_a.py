# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 15:54:07 2019

@author: kjh1
"""

T= int(input())

for t in range(T):
    
    n,m = map(int,input().split())
    
    ans = 1
    cur = 0
    
    
    for i in range(m):
        
        cur = n + m-i 
        ans = ans*cur
    
    
    if(ans>10**6):
        print('Case #{}: {}'.format(t+1,0))
        
    else:
        print('Case #{}: {}'.format(t+1,1/ans))
    
    

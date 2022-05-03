# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 09:40:23 2019

@author: kjh1
"""

T = int(input())
    
for t in range(T):
    
    n,m = map(int,input().split())
    
    total = n*(n-1)//2
    
    
    for _ in range(m):
    
        c,d = map(int,input().split())
    
    
    ans = m + (n-m-1)*2
    
    print('Case #{}: {}'.format(t+1,ans))
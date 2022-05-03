# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 11:31:30 2019

@author: kjh1
"""
import sys

T = int(input())


for t in range(T):
    
#    n,m,q = map(int,input().split())
    n,m,q = map(int,sys.stdin.readline().split())
    
#    pm =list(map(int,input().split()))
    pm = list(map(int,sys.stdin.readline().split()))
    
#    rq =list(map(int,input().split()))

    rq = list(map(int,sys.stdin.readline().split()))    

    mat = [1]*(n+1)
    mat[0] = 0
    ans = 0
    
    fn = [0]*(n+1)
    
    for i in pm:
        mat[i] = 0    
    
    
    
    for i in range(1,n+1):
        x = i
        for j in range(n//i):
            
            fn[i] += mat[x]
            x += i
            
            
    for i in rq:
        ans += fn[i]        
    
    
        
   
    print('Case #{}: {}'.format(t+1,ans))

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 11:20:08 2019

@author: kjh1
"""

T = int(input())
for t in range(T):
    NK = list(map(int,input().split()))
    A = list(map(int,input().split()))
    
    A.sort()
     
    
    ans = 0
    
    
    b = 0
    
    while(len(A)>0):
        
        for i in range(NK[1]):
            if(len(A)>0):
                del A[0]
                ans += 1
            else: break
        b += 1
        
        for j in range(len(A)):
            if(len(A)>0):
                if(A[0]<=b):
                    del A[0]
                else:
                    break
            else:
                break
        
    
    
    print('Case #{}: {}'.format(t+1,ans))
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 15:12:55 2019

@author: kjh1
"""
import sys

n = int(input())

dp1 = [0,0,0]
dp2 = [0,0,0]

for i in range(n):
    
    a,b,c = map(int,input().split())
    
#    a,b,c = map(int,sys.stdin.readline().split())
    
    if(i == 0):
        dp1[0],dp1[1],dp1[2] = a,b,c
        dp2[0],dp2[1],dp2[2] = a,b,c
        
    else:
        
        ba = a + max(dp1[0],dp1[1])
        bb = b + max(dp1[0],dp1[1],dp1[2])
        bc = c + max(dp1[1],dp1[2])
        
        sa = a + min(dp2[0],dp2[1])
        sb = b + min(dp2[0],dp2[1],dp2[2])
        sc = c + min(dp2[1],dp2[2])
        
        
        
        dp1[0],dp1[1],dp1[2] = ba,bb,bc
        dp2[0],dp2[1],dp2[2] = sa,sb,sc



big = max(dp1)
small = min(dp2)
    
print(dp2)
print(big, small)
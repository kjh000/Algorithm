# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 15:51:39 2019

@author: kjh1
"""
import sys

t = 1

while True:
    
    n = int(input())
    if(n == 0): break
    
    dp = [0,0,0]
    
    for i in range(n):
#        a,b,c = map(int,input().split())
        a,b,c = map(int,sys.stdin.readline().split())
        if(i == 0):
            dp = [0,b,b+c]
            
        elif(i == 1):
            
            xa,xb,xc = dp[0],dp[1],dp[2]
            dp[0] = a + dp[1]
            dp[1] = b + min(dp[0],dp[1],dp[2])
            dp[2] = c + min(dp[1],dp[2],xb)
            
        else:
            
            xa,xb,xc = dp[0],dp[1],dp[2]
            
            dp[0] = a + min(xa,xb)
            dp[1] = b + min(xa,dp[0],xb,xc)
            dp[2] = c + min(xb,xc,dp[1])
            
    print("{}. {}".format(t,dp[1]))
    
    t += 1
        
        
        
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 14:53:30 2019

@author: kjh1
"""
import sys

def do_dp(n,m):


    for i in range(m+1):
        for j in range(n):
            if(i - mat[j][1] >= 0):
                dp[i] = max(dp[i],dp[i-mat[j][1]] + mat[j][0])
                
    return dp[m]
                

while True:


#    n,m = map(float,input().split())
    n,m = map(float,sys.stdin.readline().split())
    n = int(n)
    m = int(m*100+0.5)
    
    
    mat = []
    dp = [0]*(m+1)
    
    if(n == 0): break
    
    
    for i in range(n):
#        c,p = map(float,input().split())
        c,p = map(float,sys.stdin.readline().split())
        c = int(c)
        p = int(p*100 + 0.5)
        mat.append([c,p])
    
    
        
    a = do_dp(n,m)
    
    print(a)
    
        
    
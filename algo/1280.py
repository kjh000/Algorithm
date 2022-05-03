# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 17:06:11 2019

@author: kjh1
"""

n = int(input())
mat = [0]
#dp = [[[0]*(n+1) for _ in range(n+1)] for _ in range(n+1)]
dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    mat.append(int(input()))
    
mat.sort()

dp[1][1] = mat[1]

for i in range(1,n+1):
    for j in range(2,n+1):
        
        if(i == j): continue
        
        dp[i][j] = dp[i-1][j] + mat[j]
        
print(dp)
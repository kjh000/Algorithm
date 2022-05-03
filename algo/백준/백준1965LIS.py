# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 03:38:04 2019

@author: kjh1
"""


n = int(input())

mat = list(map(int,input().split()))

dp = [1]*n


for i in range(n):
    
    for j in range(i):
        
        if(mat[i] > mat[j] and dp[i] <= dp[j]):
            dp[i] = dp[j] + 1
         

print(max(dp))
print(dp)
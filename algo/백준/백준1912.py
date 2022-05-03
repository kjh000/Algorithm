# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 15:58:30 2019

@author: kjh1
"""



n = int(input())

arr = [0]*n

dp = [0,0,0]


arr = list(input().split())
arr = list(map(int,arr))


dp[2] = arr[0]

for i in range(n):
    
    dp[0] = arr[i]
    dp[1] = dp[1]+arr[i]

    if(dp[1]>=dp[2]):
        dp[2] = dp[1]
    
    if(dp[1]<0):
        dp[1] = 0
    
    
print(dp[2])


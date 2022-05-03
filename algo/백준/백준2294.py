# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 16:14:23 2019

@author: kjh1
"""



n,k = map(int,input().split())

dp = [10001]*(k+1)
coin = [0]*n

for i in range(n):
    
    a = int(input())
    coin[i] = a
    if(a<=k):
        dp[a] = 1


for i in range(k+1):
    
    for j in range(n):
        
        if(i - coin[j]< 0 ):
            continue
        else:
            if(dp[i] == 1):
                continue
            else:
                if(dp[i]>dp[i-coin[j]] + 1):
                    dp[i] = dp[i - coin[j]] + 1
                
                    
                    
if(dp[k] == 10001):
    print(-1)
else:
    print(dp[k])
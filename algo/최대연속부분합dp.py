# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 16:15:28 2019

@author: kjh1
"""
n = int(input())

mat = [33,36,-73,15,43,-17,36,-28,-1,21]
#mat = list(map(int,input().split()))

dp =[0]*(n)

dp[0] = mat[0]

for i in range(1,n):
    dp[i] = max((dp[i-1]) + mat[i],mat[i])
    
print(dp)

def max_consecutive_sum_dp(arr,n):
    
    max_sum = dp[0]
    
    for i in range(n):
        if(dp[i] > max_sum):
            max_sum = dp[i]
        
    return max_sum


ans = max_consecutive_sum_dp(mat,n)

print(ans)

max_sum = max(dp)
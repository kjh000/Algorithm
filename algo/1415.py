# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 15:18:37 2020

@author: kjh1
"""

BIG = 20

n = int(input())

mat = []
dp = [0]*(BIG)
d = [0]*(BIG)
nums = [0]*(10001)
dp[0] = 1
d[0] = 1
for i in range(n):
    
    a = int(input())
    if(nums[a] == 0):
        mat.append(a)
        
    nums[a] += 1
    
for now in mat:
    for i in range(BIG-1,0,-1):
        for j in range(1,nums[now]+1):
            if(i - now*j <0): break
            dp[i] += dp[i - now*j]
            







print(dp)
print(d)
print(mat)
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 11:34:45 2019

@author: kjh1
"""



N = int(input())


matrix = [[-1]*15 for i in range(15)]

dp = [1]*15
bitmask = [1]*15
ans = [0]*15
for i in range(15):
    dp[i] |= dp[i]<<i
    bitmask[i] = dp[i] 


for i in range(N):
    for j in range(N):
        matrix[i][j] = int(input())

for i in range(N,15):
    dp[i] = 0
        


def solve(a,b,c):
    
    if matrix[a+1][b]>=0:
        for i in range(N):
            if(matrix[a+1][b+i]>=matrix[b][c+1]):
                dp[a+1]|=bitmask[i]
                
            else:   continue
        solve(a+1,b,c+1)
    else:   return dp
        
    

    
        
solve(0,0,0)
        

way = list(map(bin,dp))


for i in range(N):
    ans[i] = way[i].count('1')
    
print(max(ans))
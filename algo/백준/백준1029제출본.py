# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 11:34:45 2019

@author: kjh1
"""

N = int(input())

dp = [1]*15
bitmask = [1]*15
ans = [0]*15
for i in range(15):
    dp[i] |= dp[i]<<i
    

bitmask = dp[:]


matrix = [[int(x)for x in input()]for y in range(N)]


for i in range(N):
    for j in range(15-N):
        matrix[i].append(-1)
        
for i in range(15-N):
    matrix.extend([[-1]*15])
    
    


def solve(a,b,c):
    
    if(a<14):
        if matrix[a+1][b]>=0:
            for i in range(N):
                if(matrix[a+1][b+i]>=matrix[b][c+1]):
                    dp[a+1]|=bitmask[i]
                    
            solve(a+1,b,c+1)
       
solve(0,0,0)
        

way = list(map(bin,dp))

print(way)

#
#for i in range(N):
#    ans[i] = way[i].count('1')
#    
#print(max(ans))
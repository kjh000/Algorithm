# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 11:00:55 2019

@author: kjh1
"""

MN = list(map(int,input().split()))



matrix = [[0]*MN[1] for i in range(MN[0])]
dp = [[0]*MN[1] for i in range(MN[0])]

for i in range(MN[0]):
    matrix[i] = list(map(int,input().split()))

dp[0][0] = 1




for i in range(MN[1]-1):
    if(dp[0][i] != 0):
        if(matrix[0][i+1]<matrix[0][i]):
            dp[0][i+1] = 1
    else:
        break
       
            
for i in range(MN[0]-1):
    if(dp[i][0] != 0):
        if(matrix[i+1][0]<matrix[i][0]):
            dp[i+1][0] = 1
        else:
            break



for j in range(1,MN[0]):
    for i in range(1,MN[1]):
 
        if((dp[j][i-1] != 0) and (matrix[j][i]<matrix[j][i-1])):
            dp[j][i] = dp[j][i] + dp[j][i-1]
            
        if((dp[j-1][i] != 0) and (matrix[j][i]<matrix[j-1][i])):
            dp[j][i] = dp[j][i] + dp[j-1][i]
                
        if(dp[j][i] != 0):
            if(matrix[j][i]>matrix[j][i-1]):
                dp[j][i-1] = dp[j][i-1] + dp[j][i]



print(dp)
print(dp[MN[0]-1][MN[1]-1])
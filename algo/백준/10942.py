# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 16:43:12 2019

@author: kjh1
"""
#import sys
#sys.stdin.readline()
n1 = int(input())
N = n1+1

numbers = list(map(int,input().split()))

numbers.insert(0,0)
M = int(input())

dp = [[0]*N for i in range(N)]

ans = []

for i in range(1,N):
    dp[i][i] = 1
    
for i in range(1,n1):
    if(numbers[i] == numbers[i+1]):
        dp[i][i+1] = 1


for i in range(2,n1):
    for j in range(1,N):
        if(i+j>n1):
            continue
        else:
            if(numbers[j] == numbers[j+i]):
                if(dp[j+1][j+i-1]==1):
                    dp[j][j+i] = 1


            

for i in range(M):
    SE = list(map(int,input().split()))
    ans.append(dp[SE[0]][SE[1]])
    
for i in range(M):
    print(ans[i])


        
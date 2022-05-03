# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 16:30:41 2019

@author: kjh1
"""
import sys

n,m,k = map(int,input().split())

food = [[0]*(n+1) for _ in range(n+1)]
dp = [[0]*(n+1) for _ in range(n+1)]


route = {}


for i in range(n):
    route[i+1] = []


for i in range(k):
    a,b,c = map(int,input().split())
#    a,b,c = map(int,sys.stdin.readline().split())
    
    if(a>b): continue

    if(food[a][b] == 0):
        route[a].append(b)
        

    food[a][b] = max(food[a][b],c)

for i in range(n):
    route[i+1].sort()


for i in range(len(route[1])):
    dp[route[1][i]][1] = food[1][route[1][i]]
    

cur = 2
for i in range(2,n):
    
    if(cur > m):
        break
    for j in range(len(route[i])):
        dp[route[i][j]][cur] = max(dp[route[i][j]][cur],dp[i][cur-1] + food[i][route[i][j]])
        
    cur += 1
        
        
        
        
print(max(dp[n]))
        
        
#1 - 2 3 4 5
#2 - 4 5
#3 - 4
#4 - 5
#
#  1 2 3 4 5
#1
#2 1     
#3 2
#4 1
#5 5
#      
#
#1- 2 3
#2 -3
#
#  1  2  3
#1 
#2 5
#3 10 8
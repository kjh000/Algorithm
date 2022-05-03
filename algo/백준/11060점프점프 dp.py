# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 13:42:13 2019

@author: kjh1
"""
import sys

n = int(input())

#mat = list(map(int,input().split()))
mat = list(map(int,sys.stdin.readline().split()))

dp = [-1]*(n+1)
dp[1] = 1


for i in range(1,n+1):
    
    for j in range(1,mat[i-1]+1):
        
        if(i+j > n ): break
        else:
            
            if(dp[i+j] < 0 ):
            
                dp[i+j] = i
            
            else:
                
                dp[i+j] = min(dp[i+j],i)


if(n == 1):
    print(0)

elif(dp[n] < 0 ):
    print(-1)
else:
    cur = dp[n]
    cnt = 1
    while True:
        
        
        if(cur == 1):
            print(cnt)
            break
        
        elif(cur == -1 or cnt >= n):
            print(-1)
            break
        
        cur = dp[cur]
        cnt += 1
        
        

#
#1 - 2
#2 - 3 , 2 - 4
#4 - 5
#5 - 6, 5 - 7, 5 - 8
#6 - 7, 6 - 8
#7 - 8
#8 - 9, 8 - 10
#9 - 10
#
#1 2 3 4 5 6 7 8 9 10
#
#1 1 1 2 4 5 5 5 8 8
#
#8
#5
#4
#2
#1
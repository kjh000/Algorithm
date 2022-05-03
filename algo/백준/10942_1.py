# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 14:07:05 2019

@author: kjh1
"""
import sys

N = int(sys.stdin.readline())

numbers = list(sys.stdin.readline().split())
numbers = list(map(int,numbers))
numbers.insert(0,0)
Q = int(sys.stdin.readline())

dp_arr = [0]*Q


def isP2(i):
   
    if(len(dp) == 1):
            dp_arr[i] = 1
            return 
    else:
        if(len(dp) == 2):
            if(dp[0] == dp[1]):
                    dp_arr[i] =1
                    return 
            else:
                    dp_arr[i] = 0
                    return 
        elif(dp[0] == dp[-1]):
            del dp[0]
            del dp[-1]
            isP2(i)
            
        else:
            dp_arr[i] = 0
            return 
                
for i in range(Q):
   
    se = list(sys.stdin.readline().split())
    se = list(map(int,se))
    
    if(Q>1):
        if(se[0]>=2000|se[1]>=2000):
            dp_arr[i] = 0
        else:
            dp = numbers[se[0]:se[1]+1]
        isP2(i)
    else:
        dp_arr[i] = 1
   
    
                    
for i in range(Q):
    print(dp_arr[i])
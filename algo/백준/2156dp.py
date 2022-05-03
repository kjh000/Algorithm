# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 11:03:51 2019

@author: kjh1
"""

n = int(input())

mat = []

dp = [0]*n

two,end = 0,0 

for i in range(n):
    mat.append(int(input()))
    
    
    
for i in range(n):
    if(i == 0):
        dp[i] = mat[i]
    elif(i == 1):
        dp[i] = dp[i-1] + mat[i]
        end = 1
        two = 1
        
    else:
        
        if(end == 0):
            dp[i] = dp[i-1] + mat[i]
            end = 1
            two = 0
        else:
            if(two == 0):
                dp[i] = dp[i-1] + mat[i]
                end = 1
                two = 1
            else:
                if(mat[i-1]>mat[i-2]):
                    if(mat[i]>mat[i-2]):
                        dp[i] = dp[i-1] - mat[i-2] + mat[i]
                        end = 1
                        two = 1
                    else:
                        dp[i] = dp[i-1]
                        end = 0
                        two = 0
                        
                    
                    
                else:
                    if(mat[i] > mat[i-1]):
                        dp[i] = dp[i-1] - mat[i-1] + mat[i]
                        end = 1
                        two = 0
                    else:
                        dp[i] = dp[i-1]
                        end  = 0
                        two = 0
                        

print(dp)
                    
            
        
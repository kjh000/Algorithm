# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 16:40:14 2019

@author: kjh1
"""


memo = [0]*1000001


n = int(input())


for i in range(1,n+1):
    
    if(i == 1):
        memo[i] = 0
    elif(i<=3):
        memo[i] = 1
        
    else:
        if(i%3 == 0):
            memo[i] = min((memo[i//3] + 1),memo[i-1]+1)
        else:
            if(i%2 == 0):
                memo[i] = min(memo[i-1]+1,memo[i//2]+1)
            else:
                memo[i] = memo[i-1] +1
            


    
        
print(memo[n])





# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 11:28:38 2019

@author: kjh1
"""



T = int(input())

output = [0]*T


for m in range(T):
    
    N = int(input())

    datatset = list(map(int,input()))
    
    
    if(N%2 == 0):
        
        dp = [[0] for i in range((N//2)+1)]
        dp[0] = sum(datatset[0:(N//2)])
            
        
        for i in range((N//2)):
           
            dp[i+1] = dp[i] - datatset[i] + datatset[i+(N//2)]
            
            
        output[m] = max(dp)
        
        
    else:
        
        dp = [[0] for i in range((N//2)+1)]
        dp[0] = sum(datatset[0:(N//2)+1])
            
        
        for i in range((N//2)):
          
            dp[i+1] = dp[i] - datatset[i] + datatset[i+(N//2)+1]
            
            
        output[m] = max(dp)
        
        
for i in range(T):
            
    print("Case #{}: {}".format(i+1,output[i]))
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 10:38:34 2019

@author: kjh1
"""

T = int(input())

output = [0]*T

for m in range(T):
    
    
    NP = list(map(int,input().split()))
    prefixes = [[] for i in range(NP[1])]
    
    
    for i in range(NP[1]):
        prefixes[i] = input()
        
    ans = 2**NP[0]
        
    prefixes.sort(key = len)
    
    
    for i in range(NP[1]):
        
        for j in range(NP[1]):
            
            if(prefixes[j].startswith(prefixes[i])):
                
                prefixes[j] = prefixes[i]
    
    set_pre = set(prefixes)
    prefixes = list(set_pre)
    
    
    
    num = [1]*len(prefixes)
    
    for i in range(len(prefixes)):
        num[i] = NP[0] - len(prefixes[i])
        ans = ans - 2**num[i]
        
    
    output[m] = ans
    
    del prefixes
    del set_pre
    del NP
    
    

for i in range(T):
    print("Case #{}: {}".format(i+1,output[i]))
    
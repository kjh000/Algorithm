# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:52:41 2019

@author: kjh1
"""


T = int(input())

for t in range(T):
    n = int(input())
    name = []
    
    chars = [[] for i in range(n)]
    difference = [0]*n
    i = 0
    s = 0
    
    for i in range(n):
    
        name.append(input())
    
    
    for i in range(n):
        
        for j in range(len(name[i])):
            
            if(name[i][j] == ' ' or name[i][j] in chars[i]):
                pass
            
            else:
                chars[i].append(name[i][j])
                difference[i] += 1
                
            
    
    maxi = max(difference)
    
    for i in range(n):
        if(difference[i] < maxi):
            name[i] = 'Z'*20
        
    ss = sorted(name)
    
    ans = ss[0]
    
    print('Case #{}: {}'.format(t+1,ans))
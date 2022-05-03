# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 09:45:45 2019

@author: kjh1
"""

T = int(input())

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for t in range(T):
    
    w = str(input())
    
    dyc = [None]*len(w)
    
    i = 1
    j = -2
    ans = ''
    dyc[1] = w[0]
    dyc[-2] = w[-1]
    
    if(len(w)%2 == 1):
        print('Case #{}: AMBIGUOUS'.format(t+1))
    else:
    
        while(i<len(w)-1):
            
            if(alpha.index(w[i+1]) - alpha.index(dyc[i]) >= 0):
                dyc[i+2] = alpha[alpha.index(w[i+1]) - alpha.index(dyc[i])]
            else:
                dyc[i+2] = alpha[alpha.index(w[i+1]) - alpha.index(dyc[i]) + 26]
        
            i += 2            
    
    
        while(-(len(w))<j):
            
            if(alpha.index(w[j-1]) - alpha.index(dyc[j]) >= 0):
                dyc[j-2] = alpha[alpha.index(w[j-1]) - alpha.index(dyc[j])]
            
            else:
                dyc[j-2] = alpha[alpha.index(w[j-1]) - alpha.index(dyc[j]) + 26]
                
            j -= 2
            
        for k in range(len(dyc)):
            ans += dyc[k]
            
        print('Case #{}: {}'.format(t+1,ans))
            

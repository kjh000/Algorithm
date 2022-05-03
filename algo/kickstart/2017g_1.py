# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 10:50:59 2019

@author: kjh1
"""



T = int(input())

for t in range(T):
    anp = list(map(int,input().split()))
    
    ans = 0
    n = 1

    
    if(anp[2] == 1):
        ans = 0
        
    else:
            
        
        for i in range(1,anp[1]+1):
            n = n*i
                
        
        if(n%(anp[2]-1) == 0):
            np = 2
        else:
            np = n%(anp[2]-1)
        
        
        
        
        
        
        ans = ((min(anp[0],abs(anp[0]-anp[2])))**np)%anp[2]
        
    
    print('Case #{}: {}'.format(t+1,ans))
    
    
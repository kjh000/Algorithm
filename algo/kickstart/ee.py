# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 17:26:57 2019

@author: kjh1
"""


T =int(input())
for t in range(T):
    
    N = int(input())
    
    N1 = N
    
    ans = 0
    
    b = 0
    k = 0
    
    def sum_r(r,n):
        
        return (r**n -1)//(r-1)





    while( k <20):
        
        nn = int(N1**(1/2))
        
        
        if(nn <3):
            nn = 2
        
        for i in range(100):
            
            b = sum_r(nn,i)
            if(b == N):
                ans = nn
                break
            elif(b > N):
                break
            
#        if(b == N):
#            break
#        
        N1 = nn
        
        k += 1
        
        
        
    if(ans == 0):
        ans = N-1
        
        
    print('Case #{}: {}'.format(t+1,ans))
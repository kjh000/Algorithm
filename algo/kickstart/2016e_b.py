# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 13:37:39 2019

@author: kjh1
"""

T =int(input())
for t in range(T):
    
    N = int(input())
    
    ans = 0
    ans1 = 0
    
    b= 0
    k = 2
    bb = 0
    
    def sum_r(r,n):
        
        return (r**n -1)//(r-1)
    
    
    
    for i in range(2,4000):
        
        
        
        for j in range(1,100):
            b = sum_r(i,j)
            if(sum_r(i,j) == N):
                ans = i
                break
            elif(sum_r(i,j) > N):
                
                b = sum_r(i,j)
                break
                
        if( b == N):
            break
        
        
        
#        
#    
#    while(k <= N+1):
#    
#        
#        for j in range(1,1001):
#            bb = sum_r(k,j)
#            if(sum_r(k,j) == N):
#                ans1 = k
#                break
#            elif(sum_r(k,j) > N):
#                
#                bb = sum_r(k,j)
#                break
#        
#        if(bb == N):
#            break
#        
#        k = k**2 -1
#                
#    
    
    
    if(ans == 0):
        ans = N-1
        
#    if(ans1 == 0):
#        ans1 = N-1

    
#    ans = min(ans,ans1)
#    ans = ans1
    print('Case #{}: {}'.format(t+1,ans))
        
    
        
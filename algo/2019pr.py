# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 16:11:56 2019

@author: kjh1
"""
big = (10**9)+7

T = int(input())
for t in range(T):
    
    n,k,x1,y1,c,d,e1,e2,f = map(int,input().split())
    
    a = []
    b = []
    ans = 0
    
    for i in range(n):
        
        if(i == 0):
         a.append((x1 + y1)%f%big)
         xx = x1
         xy = y1
         
        else:
            x = ((c*xx + d*xy + e1)%f)%big
            y = ((d*xx + c*xy + e2)%f)%big
            
            a.append((x+y)%f)
            xx = x
            xy = y
            
            
    
            
    a.reverse()
    
    
    for i in range(n):
        
        a[i] = ((i+1)*a[i])%big
        
        if(i == 0):
            b.append(a[i])
        else:
            b.append(b[i-1] + a[i])
            
        
    b.reverse()
    
    
    for i in range(n):
        
        if(i == 0):
            ans += (b[i]*k)%big
        else:
            ans += (b[i]*(i+1)*(((i+1)**k)-1)//i)%big
         
    
    print('Case #{}: {}'.format(t+1,ans%big))

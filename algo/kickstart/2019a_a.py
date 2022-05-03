# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 10:31:25 2019

@author: kjh1
"""

T= int(input())
for t in range(T):
    
    n,p = map(int,input().split())
    s = list(map(int,input().split()))
    
    a = []
    b = []
    
    ss = s
    ss.sort()
    
    
    for i in range(n-p+1):
        
        if(i == 0):
            
            a.append(sum(s[0:p]))
            
        else:
            a.append(a[i-1]-ss[i-1] + ss[i+p-1])
            
    
    for i in range(n-p+1):
    
        b.append(p*ss[i+p-1] - a[i])
        if(p*ss[i+p-1] - a[i] == 0):
            break
        
    
    
    
    
    
    
    
    print('Case #{}: {}'.format(t+1,min(b)))
          
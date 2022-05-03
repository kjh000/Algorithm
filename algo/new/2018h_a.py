# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 10:15:43 2019

@author: kjh1
"""

T =int(input())
for t in range(T):
    n,p = map(int,input().split())
    
    f = []
    prefix = 0
    
    for i in range(p):
        
        pr = input()
        lf = len(f)
        if(i == 0):
            f.append(pr)
            
        else:
            for i in range(lf):
                
                if(len(f[i]) <= len(pr)):
                    if(f[i] == pr[:len(f[i])]):
                        break
                    else:
                        if(i == lf-1):
                            f.append(pr)
                else:
                    if(f[i][:len(pr)] == pr):
                        f[i] = pr
                        break
                    else:
                        if(i == lf-1):
                            f.append(pr)
                            
     
    for i in range(len(f)):
       prefix += 2**(n - len(f[i])) 
       
    ans = 2**n - prefix
        
    print('Case #{}: {}'.format(t+1,ans))
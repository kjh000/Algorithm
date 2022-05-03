# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 18:57:25 2019

@author: kjh1
"""

T = int(input())
for t in range(T):
    
    e , n = map(int,input().split())
    s = list(map(int,input().split()))
    
    h = 0
    s.sort()
    i = 0
    
    if( e > s[0]):
        
        while(s):
            if(e>s[i]):
                e -= s[i]
                h += 1
                del s[i]
            elif(e<=s[i] and h>0):
                if(len(s)>1):
                    e += s[-1]
                    h -= 1
                    del s[-1]
                else:   break
            else:
                del s[i]
    
    
    
    
    
    
    print('Case #{}: {}'.format(t+1,h))
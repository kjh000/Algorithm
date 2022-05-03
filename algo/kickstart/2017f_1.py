# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 14:02:49 2019

@author: kjh1
"""

T = int(input())
for t in range(T):
    n = int(input())
    nlist = list(map(int,input().split()))
    
    
    global do
    do = 0
    
    
    def kicksort(a):
        global do
        
        
        if(len(a)<=1):
            
            return a
        else:
            b = []
            c = []
            if(len(a)%2 == 0):
                p = a[(len(a)//2)-1]
                e = (len(a)//2)-1
            else:
                p = a[(len(a)//2)]
                e = (len(a)//2)
            for i in range(len(a)):
                if(i == e):
                    continue
                else:
                    if(a[i]<=p):
                        b.append(a[i])
                    else:
                        c.append(a[i])
            do +=1
            return kicksort(b) + [p] + kicksort(c)
    
    
    
    ans = kicksort(nlist)
    if(do == len(ans) - 1):
        print('Case #{}: YES'.format(t+1))
    else:
        print('Case #{}: NO'.format(t+1))


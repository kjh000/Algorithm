# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 17:42:22 2019

@author: kjh1
"""


T = int(input())


for t in range(T):
    
    nm = list(map(int,input().split()))
    
    mat = [[] for i in range(nm[0])]
    small = []
    
    total = 0
    
    for i in range(nm[0]):
#        mat[i] =  list(map(int,input().split()))
        small.append(list(map(int,input().split())))
        
        
    for i in range(nm[1]-1):
        
        total += min(small[0])
        
        if(small[0][0]>=small[0][-1]):
            del small[0][-1]
        else:
            del small[0][0]
            
    print('Case #{}: {}'.format(t+1,total))

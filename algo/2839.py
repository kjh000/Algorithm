# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 15:48:33 2019

@author: kjh1
"""

mat = [-1]*(5001)

n = int(input())

for i in range(1001):
    for j in range(1667):
        
        if(i*5 + j*3 >5000):
            break
        
        if(mat[i*5 + j*3] == -1):
            mat[i*5 + j*3] = i+j
            
        else:
            mat[i*5 + j*3] = min(mat[i*5 + j*3] , i+j)
        
            
            
            
            
print(mat[n])
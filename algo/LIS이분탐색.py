# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 03:01:42 2019

@author: kjh1
"""
import bisect

n = int(input())

mat = list(map(int,input().split()))

vector = []
vector.append(mat[0])

cur = 0



for i in range(1,n):
    
    if(vector[-1] < mat[i]):
        vector.append(mat[i])
        
    elif(vector[-1] == mat[i]):
        pass
        
    
    else:
        idx = bisect.bisect(vector,mat[i])
        
        
        if(mat[i] <= vector[idx] and mat[i] != vector[idx-1]):
        
            vector[idx] = mat[i]
        

print(len(vector))

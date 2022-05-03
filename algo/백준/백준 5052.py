# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 14:38:18 2019

@author: kjh1
"""
import sys

T = int(input())

for t in range(T):
    
    n = int(input())
    
    mat = []
    
    for i in range(n):
        mat.append(input())
#        mat.append(str(sys.stdin.readline()))
        
    ans = 'YES'
        
    
    mat.sort()
    
    for i in range(n-1):
        
        if(len(mat[i]) >= len(mat[i+1])):
            pass
        
        elif(mat[i] == mat[i+1][:len(mat[i])]):
            
            ans = 'NO'
            break
            
        else:
            pass
        
    print(ans)
    
    
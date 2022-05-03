# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 19:27:03 2020

@author: kjh1
"""

mat = [[0,0] for _ in range(10**4 + 1)]

mat[1][1] = 1
mat[2][0] = 1

for i in range(3,10001):
    mat[i][0] = mat[i-1][0] + mat[i-1][1]
    mat[i][1] = mat[i-1][0]
    
n = int(input())

print(sum(mat[n]))
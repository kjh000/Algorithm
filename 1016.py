# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 16:17:10 2019

@author: kjh1
"""

a,b = map(int,input().split())

last = 10**6
BIG = 10**12 + 10**6

sqr = []
cnt = 0

mat = []

for i in range(1,last+1):
    if(i**2 > b):
        break
    
    sqr.append(i**2)
    
     
sqr.sort()
    
for i in sqr:
    for j in range(1,last+1):
        
        if(i*j > BIG):
            break
        else:
            mat.append(i*j)
            
mat.sort()
matt = mat[1:]

            
for i in matt:
    if(i >= a):
        if(i<= b):
            cnt += 1
        else:
            break
        
print(sqr)
print(mat)
print(cnt)
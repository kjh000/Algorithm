# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:27:16 2020

@author: kjh1
"""

MAX = 100
n = 100
ret = []

minFactor = [0]*(MAX+1)
minFactor[0],minFactor[1] = -1,-1
def eratos():
    for i in range(2,n+1):
        minFactor[i] = i
    
    sqrtn = int(n**(0.5))
    for i in range(2,sqrtn+1):
        if minFactor[i] == i:
            for j in range(i*i,n+1,i):
                if minFactor[j] == j:
                    minFactor[j] = i
            
def factor(n):
    while n>1:
        ret.append(minFactor[n])
        n /= minFactor[n]
        n = int(n)
        
    return ret
eratos()
factor(10)

print(ret)
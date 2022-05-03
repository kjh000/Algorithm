# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:19:11 2020

@author: kjh1
"""

ret = []

def factor(n):
    sqrtn = int(n**(0.5))
    for div in range(2,sqrtn+1):
        while n%div == 0:
            n /= div
            n = int(n)
            ret.append(div)
        
    if n >1:
        ret.append(n)
        
    return ret
            
factor(20)
print(ret)
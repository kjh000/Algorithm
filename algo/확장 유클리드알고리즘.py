# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 17:07:33 2019

@author: kjh1
"""

def gcd(A,B):
    if(B == 0): return A
    
    return gcd(B,A%B)





def extended_gcd(A,B):
    tmpA = A
    t1 , t2 = 0,1
    while B!= 0:
        q = A//B
        r = A%B
        t = t1 - q*t2
        A = B
        B = r
        t1 =t2
        t2 = t
        
        
    while t1<0 :
        t1 +=tmpA
        
    
    return t1


print(extended_gcd(1337,23))
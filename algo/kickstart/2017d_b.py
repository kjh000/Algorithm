# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 15:48:11 2019

@author: kjh1
"""

T =int(input())

n,k,a1,b1,c,d,e1,e2,f = map(int,input().split())

a =[]
b = []

rr = 0
ss = 0
xx = a1
yy = b1

for i in range(1,n+1):
    
    if(i == 1):
        
        
        a.append(a1)
        b.append(b1)
    else:
        xi = (c*xx + d*yy + e1)%f
        yi = (d*xx + c*yy + e2)%f
        ri = (c*rr + d*ss + e1)%2
        si = (d*rr + c*ss + e2)%2
        
        a.append(((-1)**ri)*xi)
        b.append(((-1)**si)*yi)
        
        xx = xi
        yy = yi
        
        

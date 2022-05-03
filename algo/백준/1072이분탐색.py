# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 14:02:11 2019

@author: kjh1
"""

x,y = map(int,input().split())

z = int(100*(y/x))

start,end = 0,10**9


while start<end:
    
    mid = (start + end)//2
#    print(mid)
    
    zz = int(100*((y+mid)/(x+mid)))
    
    
    if(x == y):
        mid = -1
        break
    
    
    
    if(z == zz):
        start = mid + 1
    
    else:
        
        if(mid +1 == end or mid == 1 or mid == 10**9):
            break
        else:
            end = mid
        

if(mid == 10**9):
    mid = -1

print(mid)
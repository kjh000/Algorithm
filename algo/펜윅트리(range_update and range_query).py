# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 14:01:26 2019

@author: kjh1
"""
N = 10
tadd = [0]*(N+1)
tmul = [0]*(N+1)

def inupadate(at,mul,add):
    if(at<1 or at>N): return
        
    while(at<=N):
        tmul[at] += mul
        tadd[at] += add
        
        at += at&-at
        
def range_update(l,r,by):
    inupadate(l,by,-by*(l-1))
    inupadate(r+1,-by,by*r)
    
def range_query(at):
    if(at==0): return 0
    if(at<1 or at>N): return 
    
    mul,add = 0,0
    
    i = at
    while i>0: 
        mul +=tmul[i]
        add += tadd[i]
        i -= i&-i

    return at*mul + add


range_update(1,4,1)
print(range_query(4))

print(range_query(0))
#range_update(1,1,5)
#print(range_query(4))
#
#print(range_query(4)-range_query(2))
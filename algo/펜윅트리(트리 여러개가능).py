# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 14:01:26 2019

@author: kjh1
"""
"""
if N = 10 ,  tree range : 1 ~ 10
"""
N = 10
add1 = [0]*(N+1)
mul1 = [0]*(N+1)


add2 = [0]*(N+1)
mul2 = [0]*(N+1)


def inupadate(at,mul,add,tmul,tadd):
    if(at<1 or at>N): return
        
    while(at<=N):
        tmul[at] += mul
        tadd[at] += add
        
        at += at&-at
        
def range_update(l,r,by,tmul,tadd):
    inupadate(l,by,-by*(l-1),tmul,tadd)
    inupadate(r+1,-by,by*r,tmul,tadd)
    
def range_query(at,tmul,tadd):
    if(at==0): return 0
    if(at<1 or at>N): return 
    
    mul,add = 0,0
    
    i = at
    while i>0:
        mul +=tmul[i]
        add += tadd[i]
        i -= i&-i

    return at*mul + add


range_update(1,10,1,mul1,add1)
range_update(1,10,2,mul2,add2)

print(range_query(10,mul1,add1))
print(range_query(10,mul2,add2))
#
#print(range_query(4)-range_query(2))
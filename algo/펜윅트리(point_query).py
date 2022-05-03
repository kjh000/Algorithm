# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 13:45:38 2020

@author: kjh1
"""
"""
if n == 10 -> tree range : 0 ~ 9
"""
N = 10

tree = [0]*(N+1)

def inupdate(x,v):
    x += 1
    while(x < N+1):
        tree[x] += v
        x += x & -x
        
def range_update(l,r,v):
    inupdate(l,v)
    inupdate(r+1,-v)
    
def point_query(x):
    x += 1
    ret = 0
    while x:
        ret += tree[x]
        x -= x & -x

    return ret


range_update(1,9,1)

print(point_query(9))   

#print(tree)
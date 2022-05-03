# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 12:35:56 2020

@author: kjh1
"""
import sys

N = 10**5 + 10
n = int(input())

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


for i in range(n):
    l,r = map(int,input().split())
    
    left = point_query(l)
    right = point_query(r)
    
    print(left + right)
    
    range_update(l,l,-left)
    range_update(r,r,-right)
    
    range_update(l+1,r-1,1)
    
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:09:53 2019

@author: kjh1
"""
import math
#
#n,m,k = map(int,input().split())
#
#logh = math.log2(n)
#h = round(logh + 0.5)
#tree_size = 2**h
#
#numbers = []
#query = []

#tree = [-1]*(2*tree_size)


#for i in range(n):
#    
#    numbers.append(int(input()))
    
#for i in range(n+k):
#    
#    query.append(list(map(int,input().split())))
#    
tree = [None]*14

def build(a,v,start,end):
    
    if (start == end):
        
        tree[v] = a[start]

    else:
        mid = (start + end)//2
        build(a,v*2, start,mid)
        
        build(a,v*2 + 1,mid+1,end)
        tree[v] = min(tree[2*v],tree[2*v+1])
        
    return tree

build([18,17,13,19,15,11,20],1,0,6)

print(tree)
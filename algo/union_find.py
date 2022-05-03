# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 10:55:47 2019

@author: kjh1
"""

n,m = map(int,input().split())

parent = [0]*(n+1)
dist = [0]*(n+1)

for i in range(n+1):
    parent[i] = i
    
def get_parent(a):
    if(parent[a] == a):
        return a
    else:
#        dist[a] += dist[parent[a]]
        parent[a] = get_parent(parent[a])        
        return parent[a]
    
def union(a,b):
    a = get_parent(a)
    b = get_parent(b)
    
    if(a < b):
        parent[b] = a
    else:
        parent[a] = b
        
def find(a,b):
    a = get_parent(a)
    b = get_parent(b)
    
    if(a ==b): return 1
    else: return -1  
    

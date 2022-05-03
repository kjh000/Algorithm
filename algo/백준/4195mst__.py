# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 13:17:05 2019

@author: kjh1
"""

f = int(input())


parent = {}
size = {}

def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return p
    
def union(x,y):
    
    x = find(x)
    y = find(y)
    
    if x!= y:
        parent[y] = x
        size[x] += size[y]
        
        
def find_root(x):
    if x == parent[x]:
        return x
    else:
        return find_root(parent[x])
    
    
for i in range(f):

    name1,name2 = input().split()
    
    if name1 not in parent:
        parent[name1] = name1
        size[name1] = 1
        
    if name2 not in parent:
        parent[name2] = name2
        size[name2] = 1
        
        
    union(name1,name2)
    
    print(size[find_root(name1)])
    
print(parent)
print(size)

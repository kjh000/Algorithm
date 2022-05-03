# -*- coding: utf-8 -*-


n = int(input())

parent = [0]*(n+1)
rank = [0]*(n+1)

for i in range(n+1):
    parent[i] = i
    
def get_parent(a):
    if(parent[a] == a):
        return a
    else:
        rank[a] += rank[parent[a]]
        parent[a] = get_parent(parent[a])        
        return parent[a]
    
def union(a,b):
    a = get_parent(a)
    b = get_parent(b)
    
    
    if(rank[a] < rank[b]):
        parent[b] = a
    else:
        parent[a] = b
        
    if rank[a] == rank[b]:
        
        rank[b] += 1
def find(a,b):
    a = get_parent(a)
    b = get_parent(b)
    
    if(a ==b): return 1
    else: return -1  
    
for i in range(n):
    x,y = map(int,input().split())
    

print(parent)    
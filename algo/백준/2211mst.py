# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 16:37:21 2019

@author: kjh1
"""
import sys

parent = {}
rank = {}

def make_set(v):
    parent[v] = v
    rank[v] = 0
    
def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
        
    return parent[v]



def union(v,u):
    
    root1 = find(v)
    root2 = find(u)
    
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            
            if rank[root1] == rank[root2]:
                rank[root2] += 1
                
                
def kruskal(graph):
    for v in graph['vertices']:
        make_set(v)
        
    mst = []
    
    edges = graph['edges']
    edges.sort()
    
    for edge in edges:
        weight,v, u = edge
        
        if find(v) != find(u):
            union(v,u)
            mst.append(edge)
            
    return mst


graph = {
        'vertices' : [],
        'edges' : []       
        }





n,m = map(int,input().split())

for i in range(n):
    
    graph['vertices'].append(i+1)

for i in range(m):
    
#    a,b,c = map(int,input().split())
    a,b,c = map(int,sys.stdin.readline().split())
    
    
    graph['edges'].append((c,a,b))
    
mat = kruskal(graph)

print(len(mat))

for i in range(len(mat)):
    print(mat[i][1],mat[i][2])

#print(mat)








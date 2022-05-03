# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:32:18 2019

@author: kjh1
"""
import sys
    
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
        
#    mst = []
    mst = 0
    
    
    edges = graph['edges']
    edges.sort()
    
    for edge in edges:
        weight,v, u = edge
        
        if find(v) != find(u):
            union(v,u)
#            mst.append(edge)
            mst += edge[0]
    return mst

T = int(input())

for t in range(T):
    n,m = map(int,input().split())
    
    parent = {}
    rank = {}
    
    def make_set(v):
        parent[v] = v
        rank[v] = 0
    
    
    graph = {
            'vertices' : [],
            'edges' : []       
            }
    
    
    
    
    for i in range(n):
        graph['vertices'].append(i+1)
        
    for i in range(m):
#        c,d = map(int,input().split())
        c,d = map(int,sys.stdin.readline().split())
        
        graph['edges'].append((1,c,d))
        
    black = kruskal(graph)
    
    ans = black + (n-1 - black)*2
    
    print('Case #{}: {}'.format(t+1,ans))
    
    
    
    

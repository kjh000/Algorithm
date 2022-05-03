# -*- coding: utf-8 -*-

T = int(input())
for t in range(T):
    n = int(input())
    
    parent = [0]*(n+1)
    rank = [0]*(n+1)
    dist = [0]*(n+1)
    
    for i in range(n+1):
        parent[i] = i
        
    def get_parent(a):
        if(parent[a] == a):
            return a
        else:
            dist[a] += dist[parent[a]]
            parent[a] = get_parent(parent[a])        
            return parent[a]
        
    dd = [0]
    def get_dist(a):
        if(parent[a] == a):
            dd[0] += dist[a]
            return 
        else:
            dd[0] += dist[a]
            get_dist(parent[a])        
            return
        
    def union(a,b):
        aa = get_parent(a)
        bb= get_parent(b)
        
        
        parent[aa] = bb
        dist[a] +=  abs(a-b)%1000
        
            
        if rank[aa] == rank[bb]:
            rank[bb] += 1
            
    def find(a,b):
        a = get_parent(a)
        b = get_parent(b)
        
        if(a ==b): return 1
        else: return -1  
        
    while True:
        line = list(input().split())
        if line[0] == 'O':
            break
        
        if line[0] == 'E':
            get_dist(int(line[1]))
            print(dd[0])
            dd[0] = 0
    
        else:
            i,j = int(line[1]),int(line[2])
            union(i,j)
    
    print(parent)
    print(rank)
    print(dist)
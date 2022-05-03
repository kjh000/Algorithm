import sys


n,m = map(int,input().split())

parent = [0]*(n+1)
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
    
def union(a,b):
    a = get_parent(a)
    b = get_parent(b)
    
    if a == b: return
    if dist[a] < dist[b]:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]
    
    if dist[a] == dist[b]:
        dist[b] += 1
    
        
def find(a,b):
    a = get_parent(a)
    b = get_parent(b)
    
    if(a ==b): return 1
    else: return -1  
    
for i in range(m):
    q,w,e = map(int,input().split())
    if q == 0:
        union(w,e)
    else:
        p = find(w,e)
        if p == 1:
            print('YES')
        else:
            print('No')
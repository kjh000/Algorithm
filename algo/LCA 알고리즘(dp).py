"""
depth : depth of node (level)
ac[x][y] : 2**y th ancestor of x
tmp : 2**(i-1)th ancestor of here
Graph : undirected
n : # of edge
m : # of query
    
swap to make depth[b] >= depth[a]
"""
import math

MAX_NODE = 10**5 + 1
depth = [0]*MAX_NODE
ac = [[0]*MAX_NODE for _ in range(20)]
graph = [[] for _ in range(MAX_NODE)]
max_level = 0



def getTree(here,parent):
    depth[here] = depth[parent] + 1
    
    ac[here][0] = parent
    
    max_level = math.floor(math.log2(MAX_NODE))
    
    for i in range(1,max_level+1):
        tmp = ac[here][i-1]
        ac[here][i] = ac[tmp][i-1]
        
    lenth = len(graph[here])
    
    for i in range(lenth):
        there = graph[here][i]
        if there != parent:
            getTree(there,here)
            

n,m  = map(int,input().split())

for i in range(n):
    start,end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)
    
depth[0] = -1
getTree(1,0)
max_level = math.floor(math.log2(MAX_NODE))

for M in range(m):
    a,b = map(int,input().split())
    
    if depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a,b = b,a
            
        for i in range(max_level,-1,-1):
            if depth[a] <= depth[ac[b][i]]:
                b = ac[b][i]
            
    lca = a
    
    if a != b:
        for i in range(max_level,-1,-1):
            if ac[a][i] != ac[b][i]:
                a = ac[a][i]
                b = ac[b][i]
            lca = ac[a][i]
            
    print(lca)
            
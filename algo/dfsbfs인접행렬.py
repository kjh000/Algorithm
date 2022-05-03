      # -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:58:31 2019

@author: kjh1
"""

q = list()


n,m,v = map(int,input().split())
dfs_visited = []
bfs_visited = []
mat = [[0]*(n+1) for i in range((n+1))]

for i in range(m):
    line = list(map(int,input().split()))
    
    
    mat[line[0]][line[1]] = 1
    mat[line[1]][line[0]] = 1 
    
    
    
def do_bfs(start):
    
    q = list()
    q.append(start)
    
    bfs_visited.append(start)
    
    while not len(q) == 0:
        
        current = q.pop()
        
        
        for i in range(1,n+1):
            if(mat[current][i] == 1 and i not in bfs_visited):
                q.append(i)
                bfs_visited.append(i)
        


def do_dfs(start):
   
    if(start not in dfs_visited):
        dfs_visited.append(start)

    for i in range(1,n+1):
        if(mat[start][i] == 1 and i not in dfs_visited):
            dfs_visited.append(i)        
            do_dfs(i)
            
do_dfs(v)
do_bfs(v)
            
for i in dfs_visited:
    print(i, end=" ")
    
print("")
    
for i in bfs_visited:
    print(i,end=" ")
    

# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 14:30:58 2019

@author: kjh1
"""
import queue

q = queue.Queue()


nmv = list(map(int,input().split()))
dfs_visited = []
bfs_visited = []
mat = [[0]*(nmv[0]+1) for i in range((nmv[0]+1))]

for i in range(nmv[1]):
    line = list(map(int,input().split()))
    
    
    mat[line[0]][line[1]] = 1
    mat[line[1]][line[0]] = 1 
    
    
    
def do_bfs(start):
    
    q = queue.Queue()
    q.put_nowait(start)
    
    bfs_visited.append(start)
    
    while not q.empty():
        
        current = q.get_nowait()
        
        
        for i in range(1,nmv[0]+1):
            if(mat[current][i] == 1 and i not in bfs_visited):
                q.put_nowait(i)
                bfs_visited.append(i)
        


def do_dfs(start):
   
    if(start not in dfs_visited):
        dfs_visited.append(start)

    for i in range(1,nmv[0]+1):
        if(mat[start][i] == 1 and i not in dfs_visited):
            dfs_visited.append(i)        
            do_dfs(i)
            
do_dfs(nmv[2])
do_bfs(nmv[2])
            
for i in dfs_visited:
    print(i, end=" ")
    
print("")
    
for i in bfs_visited:
    print(i,end=" ")
    
    
        
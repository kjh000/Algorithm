# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 10:49:15 2019

@author: kjh1
"""

T = int(input())
N = int(input())
dfs_visited = []
count = 0

mat = [[0] for i in range(N)]
edge = []
length = [[] for i in range(N//2)]

def do_dfs(start):
   
    if(start not in dfs_visited):
        dfs_visited.append(start)

    for i in range(N):
        if(mat[start][i] != 0 and i not in dfs_visited):
            dfs_visited.append(i)        
            
            do_dfs(i)



for i in range(N):
    mat[i] = list(map(int,input().split()))
    

for i in range(N):
    if(mat[i].count(0)<N-2):
        for j in range(N):
            mat[i][j] = 0
            mat[j][i] = 0


for i in range(N):
    dfs_visited.clear()
    do_dfs(i)
    if(set(dfs_visited) not in edge):
        edge.append(set(dfs_visited))
        4
for i in range(len(edge)):
    for j in range(len(edge[i])-1):
        length[i].append(mat[list(edge[i])[j]][list(edge[i])[j+1]])
    length[i].sort(reverse = True)

length.sort(reverse = True)

print(edge)
print('--'*10)
print(length)

for i in range(len(length)):
    if(len(length[i])>2):
        if(length[i][0]<sum(length[i][1:])):
            count += 1
    
        
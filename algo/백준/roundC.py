# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 12:53:02 2019

@author: kjh1
"""

N = int(input())

dfs_visited = []
stack = [1]
distance = [-1]*N
dic = dict([])
mat = [[0]*(N+1) for i in range(N+1)]

for i in range(1,N+1):
    
    V = list(map(int,input().split()))
    
    mat[V[0]][V[1]] = 1
    mat[V[1]][V[0]] = 1
    
    
    
    
for i in range(1,N+1):
    
        for j in range(1,N+1):
            if(mat[i][j] == 1):
                try:
                    dic[i].append(j)
                except KeyError:
                    dic[i] = [j]
    

def do_dfs(start):
   
    if(start not in dfs_visited):
        dfs_visited.append(start)

    for i in range(1,N+1):
        if(i != 1 and mat[start][i] == 1 and i in dfs_visited):
#            print(start)
            break
        elif(mat[start][i] == 1 and i not in dfs_visited):
            dfs_visited.append(i)        
            do_dfs(i)




do_dfs(1)

s1 = set(dic[dfs_visited[-1]])
s2 = set(dic[dfs_visited[-2]])
s3 = list(s1 & s2)[0]

distance[dfs_visited[-1] -1] = 0
distance[dfs_visited[-2] -1] = 0
distance[s3 -1] = 0

#
for i in range(N):
    for j in range(len(dic[i+1])):
        if(distance[i] != -1 and distance[dic[i+1][j]-1] == -1):
            distance[dic[i+1][j]-1] = distance[i] + 1


                  
print(distance)
            
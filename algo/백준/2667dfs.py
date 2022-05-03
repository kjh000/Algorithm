# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 18:01:57 2019

@author: kjh1
"""

n = int(input())

mat = []

stack = []
visit = [[0]*n for i in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

total = 0
home = []
h = 0


def is_safe(y,x):
    
    if(x>=n or y>=n or x<0 or y<0):
        return 0
    else:
        return 1


for i in range(n):
    
    line = list(map(int,input()))
    
    mat.append(line)
    
    
    
for i in range(n):
    
    for j in range(n):
        
        if(mat[i][j] == 0 or visit[i][j] == 1):
            pass
        else:
            
            stack.append([i,j])
            while stack:
                node = stack.pop()
                
                if(visit[node[0]][node[1]] == 0):
                
                    visit[node[0]][node[1]] = 1
                    h += 1
                    
                    for k in range(4):
                        
                        if(is_safe(node[0] + dy[k],node[1] +dx[k])==0):
                            pass
                        else:
                            if(mat[node[0] + dy[k]][node[1] + dx[k]] == 1):
                                stack.append([node[0] + dy[k],node[1]+dx[k]])
                        
                        
            total += 1
            home.append(h)
            h = 0
print(total)
home.sort()

for i in range(total):
    print(home[i])
    

            
            
            
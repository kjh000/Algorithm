# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 16:28:06 2019

@author: kjh1
"""
import sys

m,n = map(int,input().split())

mat = []
dp = [[0]*n for i in range(m)]
dp [0][0] = 1
q = []



for i in range(m):
    mat.append(list(map(int,input().split())))
#    mat.append(list(map(int,sys.stdin.readline().split())))

def is_inside(row,cul):
    
    if(row > m-1 or row <0 or cul > n-1 or cul <0):
        return 0
    
    else:
        return 1
    
dx = [1,0,-1,0]
dy = [0,1,0,-1]

q.append([0,0])


while q:
    
    cur = q.pop()
    
    for k in range(4):
        if(is_inside(cur[0]+dy[k],cur[1]+dx[k]) == 1):
            if(mat[cur[0]][cur[1]] > mat[cur[0]+dy[k]][cur[1]+dx[k]]):
#                dp[cur[0]+dy[k]][cur[1]+dx[k]] += dp[cur[0]][cur[1]]
                dp[cur[0]+dy[k]][cur[1]+dx[k]] += 1
#                q.insert(0,[cur[0]+dy[k],cur[1]+dx[k]])
                q.append([cur[0]+dy[k],cur[1]+dx[k]])
#                print([cur[0]+dy[k],cur[1]+dx[k]])
                

print(dp)
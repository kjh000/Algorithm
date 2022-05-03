# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:44:01 2019

@author: kjh1
"""

T = int(input())

n,m,p = map(int,input().split())
INF = (10**9)+1
mat = [[INF]*n for i in range(n)]
dp = [[0]*n for i in range(n)]
total = []
aa = 0
for i in range(m):
    line = list(map(int,input().split()))
    mat[line[0]-1][line[1]-1] = line[2]


for i in range(n):
    for j in range(n):
        if(mat[i][j] != -1):
            mat[j][i] = mat[i][j]
        if(i == j):
            mat[i][j] = 0






for k in range(n):
    for i in range(n):
        for j in range(n):
            if(mat[i][j] > mat[i][k] + mat[k][j]):
                mat[i][j] = mat[i][k] + mat[k][j]


for i in range(n):
    total.append(sum(mat[i]))
    if(i != 0):
        aa += total[i]
        


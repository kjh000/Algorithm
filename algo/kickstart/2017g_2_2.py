# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 23:25:26 2019

@author: kjh1
"""


T = int(input())

for t in range(T):
    N = int(input())
    r = list(map(int,input().split()))
    b = list(map(int,input().split()))
    INF = (10**9)+1
    rb = []
    visit = []
    
    for i in range(N):
        rb.append((r[i],b[i]))
    
    total = 0
    
    mini = []

    xor = [[] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if(i == j):
                xor[i].append(INF)
            else:
                xor[i].append(min((rb[i][0]^rb[j][1],rb[i][1]^rb[j][0])))
    
    
    print(xor)
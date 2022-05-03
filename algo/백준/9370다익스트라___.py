# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:15:02 2019

@author: kjh1
"""
import sys

INF = sys.maxsize

n,m,t = map(int,input().split())

s,g,h = map(int,input().split())

mat = [[INF]*n for _ in range(n)]
tt = []

for i in range(m):
    a,b,d = map(int,input().split())
    
    mat[a-1][b-1] = d
    mat[b-1][a-1] = d
    

for i in range(t):
    
    tt.append(int(input()))
    
    

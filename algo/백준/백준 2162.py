# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 17:39:52 2019

@author: kjh1
"""

n = int(input())

line = [[] for _ in range(n)]

for i in range(n):

    x1,y1,x2,y2 = map(int,input().split())
    
    line[i].append([x1,y1])
    line[i].append([x2,y2])
    
    line[i].sort(reverse=True)
    
    
line.sort(reverse = True)
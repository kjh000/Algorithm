# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 13:43:36 2019

@author: kjh1
"""
import sys

n = int(input())

mat = []
names = []

io = {}

for i in range(n):
#    a,b = input().split()
    a,b = sys.stdin.readline().split()
    
    mat.append([a,b])
    names.append(a)
    
mat.sort(reverse = True)

s_names = set(names)
l_names = list(s_names)
l_names.sort(reverse = True)

for i in l_names:
    io[i] = 0
    
for i in mat:
    io[i[0]] += 1
    
for i in io:
    
    if(io[i]%2 == 1):
        print(i)

    


    
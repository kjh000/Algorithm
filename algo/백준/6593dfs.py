# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:31:38 2019

@author: kjh1
"""

l,r,c = map(int,input().split())

lrc = []

sl,sr,sc = 0,0,0
el,er,ec = 0,0,0

dx = [1,0,0,-1,0,0]
dy = [0,1,0,0,-1,0]
dz = [0,0,1,0,0,-1]


mat = [[[0 for x in range(30)] for y in range(30)] for z in range(30)]



for i in range(l):
    
    rc = []
    
    for j in range(r):
        
        row = input()
        if('S' in row):
            sl = i
            sr = j
            sc = row.index('S')
            
        
        if('E' in row):
            el = i
            er = j
            ec = row.index('E')

        rc.append(row)
        
    lrc.append(rc)
    
    

print(lrc)

print(sl,sr,sc)

print(el,er,ec)
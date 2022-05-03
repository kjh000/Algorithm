# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:32:33 2020

@author: kjh1
"""

n = int(input())
UDLR = input()


mat = [[[0,0]for _ in range(n)]for _ in range(n)]
cross = [[0]*n for _ in range(n)]

x,y = 0,0

for i in UDLR:
    
    if(i == 'D'):
        
        if(y == n-1): continue
        
        mat[y][x][0] = 1
        mat[y+1][x][0] = 1
        
        y += 1
        
    elif(i == 'U'):
        
        if(y == 0): continue
        
        mat[y][x][0] = 1
        mat[y-1][x][0] = 1
        
        y -= 1
        
    elif(i == 'L'):
        
        if(x == 0): continue
        mat[y][x][1] = 1
        mat[y][x-1][1] = 1
        
        x -= 1
        
    elif(i == 'R'):
        if(x == n-1): continue
        mat[y][x][1] = 1
        mat[y][x+1][1] = 1
        
        x += 1
        
    else:
        continue
        
for i in range(n):
    for j in range(n):
        
        if(mat[i][j] == [1,0]): cross[i][j] = chr(124)
        elif(mat[i][j] == [0,1]): cross[i][j] = chr(45)
        elif(mat[i][j] == [1,1]): cross[i][j] = chr(43)
        else: cross[i][j] = chr(46)
        

for i in cross:
    print(''.join(i))
        
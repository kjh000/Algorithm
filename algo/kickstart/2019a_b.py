# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 16:36:25 2019

@author: kjh1
"""

#T = int(input())

r,c = map(int,input().split())
mat = [None]*r
do = []
dic = {}
doo = []
for i in range(r):
    mat[i] = list(map(int,input()))
    for j in range(c):
        if(mat[i][j] == 1):
            do.append((i,j))

for i in range(len(do)):
    doo.append((do[i][0]*c + do[i][1]+1,0))
    
dic[0] = doo
        
    
    

for i in range(1,r*c+1):
    
    if(r == 1):
        if(i == 1):
            dic[i] = [(i+1,1)]
        elif(i == c+1):
            dic[i] = [(i-1,1)]
        else:
            dic[i] = [(i-1,1),(i+1,1)]
            
    else:
        
        if(i == 1):
            dic[i] = [(i+1,1),(i+c,1)]
        elif(i == c):
            dic[i] = [(i-1,1),(i+c,1)]
        elif(i>1 and i<c):
            dic[i] = [(i-1,1),(i+1,1),(i+c,1)]
        
        elif(i>=r*c-c+1):
            if(i == r*c-c+1 ):
                dic[i] = [(i+1,1),(i-c,1)]
            elif(i == r*c):
                dic[i] = [(i-1,1),(i-c,1)]
            else:
                dic[i] = [(i-1,1),(i+1,1),(i-c,1)]
                
        else:
            if(i%c == 1):
                dic[i] = [(i+1,1),(i+c,1),(i-c,1)]
            elif(i%c == 0):
                dic[i] = [(i-1,1),(i+c,1),(i-c,1)]
            else:
                dic[i] = [(i-1,1),(i+1,1),(i+c,1),(i-c,1)]

#
#            

print(mat)
print(do)
print(dic)
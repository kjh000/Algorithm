# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 13:11:21 2019

@author: kjh1
"""

n,q = map(int,input().split())

mat = [1]*(n+1)
head = [0]*(n+1)
long = 1
mat[0] = None

link = [[0,0] for _ in range(n+1)]


for i in range(1,n+1):
    
    link[i] = [i,i]

    

for i in range(q):
    a= int(input())
    
    mat[a] = mat[a]*(-1) 
    
    if(a == 1):
        if(mat[a] != mat[a+1]):
            link[a] = [1,2]
            link[a+1][0] = a
        else:
            link[a] = [1,1]
            link[a+1][0] = a+1
    elif(a == n):
        if(mat[a] != mat[a-1]):
            link[a] = [a-1,a]
            link[a-1][1] = a
        else:
            link[a] = [a,a]
            link[a-1][1] = a-1
            
            
    else:
        if(mat[a] != mat[a-1]):
            link[a][0] = a-1
            link[a-1][1] = a
            
        else:
            link[a][0] = a
            link[a-1][1] = a-1
            
        
        if(mat[a] != mat[a+1]):
            link[a][1] = a+1
            link[a+1][0] = a
            
            
        else:
            link[a][1] = a
            link[a+1][0] = a+1
            
            
    print(mat)
    print(link)
    print(head)
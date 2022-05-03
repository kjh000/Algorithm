# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 14:36:49 2019

@author: kjh1
"""
mat = []
stack = []
visit = []

while not len(stack) == 0:
    
    current = stack.pop()
    
    for i in range(len(mat[current])):
        
        if(mat[current][i] not in visit):
            stack.append(mat[current][i])
            
    visit.append(current)

        




def do_dfs(start):
   
    if(start not in visit):
        visit.append(start)

    for i in range(len(mat[start])):
        if(mat[start][i] not in visit):
            visit.append(mat[start][i])
            do_dfs(mat[start][i])

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 10:05:34 2019

@author: kjh1
"""



def dfs(index ,string):
            
    global cnt
    
    if(cnt == 6):
        print(string)
        
    else:
        for i in range(index+1,k):
            cnt += 1
            dfs(i,string + ' '  + s[i])
            
    cnt -= 1


while True:
    
    
    mat = list(input().split())
    
    k = int(mat[0])
    s = mat[1:]
    
    if(k == 0):
        
        break
    
    else:
    
        cnt = 0
        
        
        for i in range(k-5):
            cnt = 1
            dfs(i,s[i])
            
        
        print()
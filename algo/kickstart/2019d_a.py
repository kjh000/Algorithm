# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 10:56:33 2019

@author: kjh1
"""

T = int(input())

for t in range(T):
    
    n,m = map(int,input().split())
    
    cd = []
    mat = [0 for i in range(n+1)]
    ans = 0
    num = 0
    cycle = 0
    
    for i in range(m):
        a,b = 0,0
        c,d = map(int,input().split())
        
        if(c<=d):
            a = c
            b = d
        else:
            a = d
            b = c
            
        cd.append([a,b])
        
    cd.sort()
    
    for i in range(m):
        if(i == 0):
    
            mat[cd[i][0]] += 1
            mat[cd[i][1]] += 1        
            
        else:
            mat[cd[i][1]] += 1
            
        if(mat[cd[i][1]] == 2):
            cycle = 1
            
            
    for i in range(len(mat)):
        if(mat[i] > 0 ):
            num += 1
    
    total = n*(n-1)//2
    mini = n-1
    r = total - m
    
    
    if(m <= 2):
        ans  = m + 2*(mini-m)
    else:
        if(cycle == 0):
            if(m <= mini):
                
                ans  = m + 2*(mini-m)
            else:
                ans = mini
    
        else:
            ans = num - 1 +2*(mini - (num-1))
            
    print('Case #{}: {}'.format(t+1,ans))
                        
    
            
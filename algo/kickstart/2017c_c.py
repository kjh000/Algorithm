# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:47:40 2019

@author: kjh1
"""

T = int(input())

for t in range(T):
        
    n,q = map(int,input().split())
    
    check = [0]*q
    
    aa = [0]*q
    
    a= []
    for i in range(n+1):
        a.append(input())
        
    score = list(map(int,input().split()))
    
    ans = 0
    
    if(n == 1):
        for i in range(q):
            if(a[0][i] == a[1][i]):
                check[i] = 1
                
        if(score[0]<=check.count(1)):
            ans += score[0] + q - check.count(1)
        else:
            ans += check.count(1) + q - score[0]
            
        print('Case #{}: {}'.format(t+1,ans))
    
    else:
        
        if(score[0]>=score[1]):
            big = 0
            small = 1
        else:
            big = 1
            small = 0
        for i in range(q):
            if(a[0][i] == a[1][i]):
                check[i] = 1
        
        
        for i in range(q):
            if(check[i] == 1):
                if(a[0][i] == a[2][i]):
                    aa[i] = 1
                    
        
    
          
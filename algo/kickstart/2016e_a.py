# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 09:52:13 2019

@author: kjh1
"""

T = int(input())
for t in range(T): 
    s = input()
    
    i,j = map(int,input().split())
    
    ls = len(s)
    bs = s.count('B')
    
    ii = i%ls
    jj = j%ls
    
    ans = 0
    
    if(j <= ls):
        
        ans = s[i-1:j].count('B')
        
    if(j>ls and i< ls):
        
        ans = ((j -ls)//ls)*bs
        ans += s[:jj+1].count('B')
        ans += s[i:].count('B')
        
    if(i >= ls):
        
        if(i == j):
            if(ii == 0):
                if(s[-1] == 'B'):
                    ans = 1
                else:   ans = 0
            else:
                if(s[ii-1] == 'B'):
                    ans = 1
                else:
                    ans = 0
                    
        
        else:
            if(jj == 0):
                if(ii != 0):
                    ans += ((j-(i-ii))//ls)*bs
                    
                    ans -= s[:ii-1].count('B')
                else:
                    
                    ans += ((j-(i-ii))//ls)*bs
                    
                    ans -= s[:ii].count('B')
                    ans += s[-1:].count('B')
                    
            else:
                ans += ((j+(ls-jj)-(i-ii)+1)//ls)*bs
                
                ans -= s[:ii].count('B')
                
                ans -= s[jj:ls-jj].count('B')
            
                
    print('Case #{}: {}'.format(t+1,ans))
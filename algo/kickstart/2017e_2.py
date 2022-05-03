# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 10:19:58 2019

@author: kjh1
"""

def chooese_two(n):
    
    return (n*(n-1))//2

def chooese_three(n):
    return (n*(n-1)*(n-2))//6
    

T = int(input())

for t in range(T):
    
    N = int(input())
    l = list(map(int,input().split()))
    count = []
    
    
    ans2 = 0
    
    ans4 = 0
    s = list(set(l))

    
    
    for i in range(len(s)):
        count.append(l.count(s[i]))
        
    
    for i in range(len(s)):
        if(count[i]>2):
            for j in range(len(s)):
                if(i == j):
                    pass
           
                else:
                    
                    ans2 += chooese_three(count[i])*count[j]
                   
    
            
    for i in range(len(s)):
        if(count[i]>=2):
            for j in range(len(s)):
                if(i == j ):
                    pass
                else:
                    for k in range(j+1,len(s)):
                        if(k == i):
                            pass
                        else:
                            
                            if(s[i]*2 + min(s[j],s[k])>max(s[j],s[k])):
                                ans4 += chooese_two(count[i])*count[j]*count[k]
                    
                        
        
    ans = ans2 + ans4
    
    
    print('Case #{}: {}'.format(t+1,ans))
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 12:20:00 2019

@author: kjh1
"""
from collections import defaultdict

def isAnagram(str1,str2):
    counts = defaultdict(int)
    for letter in str1:
        counts[letter]+=1
    for letter in str2:
        counts[letter] -=1
        if counts[letter]<0:
            return False
    return True
    
    
T = int(input())

for t in range(T):
    L = int(input())
    A = input()
    B = input()
    ans = 0
    
    for i in range(L):
        for j in range(L-i):
            suba = A[j:j+i+1]
            for k in range(L-i):
                subb = B[k:k+i+1]
                if(isAnagram(suba,subb)):
                    ans += 1
                    break
                
    
    
    
    
    
    
    
    print('Case #{}: {}'.format(t+1,ans))
    
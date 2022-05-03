# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 16:37:46 2019

@author: kjh1
"""

INF = 987654321

#T = int(input())

nums = input()

N = []
cache = [-1]*(10002)


for i in range(len(nums)):
    
    N.append(int(nums[i]))

def classify(a,b):
    
    M = N[a:b+1]
    
    
    progressive = True
    
    for i in range(len(M)-1):
        
        if(M[i+1] - M[i] != M[1] - M[0]):
            progressive = False
            break
        
    if(progressive == True and M[1] - M[0] == 0):
        return 1
    
    if(progressive == True and abs(M[1] - M[0]) == 1):
        return 2
    
    alternating = True
    
    for i in range(len(M)):
        if(M[i] != M[i%2]):
            alternating = False
            break
            
    if(alternating == True):    return 4
    if(progressive == True):    return 5
    
    return 10


def memorize(begin):
    
    if(begin == len(N)):    return 0
    
    if(cache[begin] != -1): return cache[begin]
    
    cache[begin] = INF
    
    for L in range(3,6):
        if(begin + L <= len(N)):
            cache[begin] = min(cache[begin], memorize(begin + L) + classify(begin, begin + L -1))
            
    return cache[begin]

print(memorize(0))
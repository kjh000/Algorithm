# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 10:32:23 2019

@author: kjh1
"""
import sys
n = list(input())
#n = list(sys.stdin.readline())
nn = len(n)

m = 0


for i in range(nn):
    n[i] = int(n[i])
    
    
n.sort(reverse = True)

for i in range(nn):
    m += n[i]
    
if(nn == 1 or m%3 != 0 or 0 not in n):
    print('-1')
    
else:
    
    
    for i in range(nn):
        n[i] = str(n[i])
    
    
    print(''.join(n))
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 14:30:38 2019

@author: kjh1
"""
import sys

n,k = map(int,input().split())

#mat = list(map(int,input().split()))
mat = list(map(int,sys.stdin.readline().split()))

psum = [0]*n
psum[0] = mat[0]
ans = 0

dic = {}
dic[k] = 0
dic[mat[0]-k] = 0
dic[mat[0]] = 0
for i in range(1,n):
    psum[i] = psum[i-1] + mat[i]
    dic[psum[i]] = 0
    dic[psum[i] - k] = 0
    
    
for i in range(n):
    if(psum[i] == k):
        ans += 1
    
    ans += dic[psum[i] - k]
    
    
    dic[psum[i]] += 1
    
print(ans)


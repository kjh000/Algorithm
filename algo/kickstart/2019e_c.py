# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 15:07:32 2019

@author: kjh1
"""
import math

BIG = 10**9


#T = int(input())



l,r = map(int,input().split())

mat = [1]*(r-l+1)

base = r-l+1
    
maxi = math.ceil(math.sqrt(r))



n=r

a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    if(i>=l):
        primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
print(primes[-1])
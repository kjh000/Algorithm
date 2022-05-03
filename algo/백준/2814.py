# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 16:41:45 2019

@author: kjh1
"""

small = 31623

n= 100
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
print(primes)

#
#3 9 27 81 243
#5 25 125 625
#7 49
#
#3 9 15 21 27
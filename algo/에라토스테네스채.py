# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 16:55:07 2019

@author: kjh1
"""
import math

n=10
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False


#
#def is_Prime(n):
#    if(n<2):
#        return False
#    
#    x = math.ceil(n**(0.5))
#    
#    for i in range(2,x+1):
#        if(n%2 == 0):
#            return False
#        
#    return True

#print(primes)

def is_Prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

if is_Prime(2):
    print('yes')
else:
    print('no')
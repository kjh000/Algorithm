# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 12:30:23 2019

@author: kjh1
"""


def facto(n):
    ans = 1
    for i in range(1,n+1):
        ans = ans*i
        
    return ans

def comb(a,b):
    
    aa = 1
    bb = facto(b)
    
    for i in range(b,a+1):
        aa = aa*i
    
    return aa//bb
    

BIG = (10**9) + 7

#T = int(input())

k = 1


n,m = map(int,input().split())

mat = [0]*(n+1)
fact = []
aa = []

mat[0] = facto(2*n)
mat[1] = facto(2*n) -2*facto(2*n-1)

for i in range(0,n+1):
    fact.append(2**(i)*facto(2*n-i))
    

for i in range(1,n+1):
    
    bb = 1
    ff = 0
    for j in range(1,i+1):
        
        ff += bb*(i-j+1)*fact[j] 
        bb = -bb
    mat[i] = mat[0] - ff
    

#for i in range(1,n+1):
#    
#    bb = 1
#    ff = 0
#    for j in range(1,i+1):
#        if(i == j):
#            ff += bb*fact[j]
#        else:
#            ff += bb*(i)*fact[j] 
#            bb = -bb
#    mat[i] = mat[0] - ff
    
    
#for i in range(2,n+1):
#    
#    mat[i] = mat[i-1] - (fact[i-1] - fact[i])
#    
    
print(mat)
#print(mat[5]%BIG)
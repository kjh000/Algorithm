# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 14:19:24 2019

@author: kjh1
"""

n = int(input())

a = []
b = []
c = []
d = []

ans = 0

for i in range(n):
    aa,bb,cc,dd = map(int,input().split())
    
    a.append(aa)
    b.append(bb)
    c.append(cc)
    d.append(dd)
    
a.sort()
b.sort()
c.sort()
d.sort()

print(a)
print(b)
print(c)
print(d)

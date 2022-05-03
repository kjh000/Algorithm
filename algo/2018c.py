# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 11:01:02 2019

@author: kjh1
"""

#T = int(input())

l = int(input())

lines = list(input().split())

s1,s2,n,a,b,c,d = input().split()

n,a,b,c,d = int(n),int(a),int(b),int(c),int(d)

x1,x2 = ord(s1),ord(s2)

s = []
s.append(s1)
s.append(s2)

for i in range(n):
    if(i < 2):
        
        xx1 = x2
        xx2 = x1
    else:
        x = (a*xx1 + b*xx2 + c)%d
        s.append(chr(97 + x%26))
       
        xx2 = xx1
        xx1 = x

st = ''.join(s)

print(st)





    

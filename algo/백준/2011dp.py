# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 19:33:47 2020

@author: kjh1
"""

MOD = 10**5

n = input()
ln = len(n)
rs = {}
ret = [0]*(ln+1)
for i in range(ln):
    if i == 0:
        rs[i+1] = n[-1]
    else:
        rs[i+1] = n[-i-1] + rs[i]

ret[1] = 1

def check(n):
    
    if n >=ln : return
    s = rs[ln - n]
    
    ret[n+1] = ret[n+1] + ret[n]
    check(n+1)
#    print('{} : 1'.format(n+1))
    if len(s) >= 2:
        if int(s[:2]) <=26 :
#            ret[n+2] = ret[n+2] + ret[n]
            check(n+2)
#            print('{} : 2'.format(n+2))
    
    
check(0)

print(ret)
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 18:11:50 2019

@author: kjh1
"""

def CCW(p1,p2,p3):
    
    op = p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1]
    
    op -=(p1[0]*p3[1] + p2[0]*p1[1] + p3[0]*p2[1])
    
    if(op > 0): return 1
    elif(op == 0): return 0
    else: return -1
    


a1 = [1,1]
a2 = [3,3]

b1 = [0,2]
b2 = [2,0]

c1 = CCW(a2,a1,b1)
c2 = CCW(a2,a1,b2)

print(c1*c2)
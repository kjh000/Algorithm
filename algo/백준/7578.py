# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 13:41:16 2019

@author: kjh1
"""
import sys

n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

#a = list(map(int,sys.stdin.readline().split()))
#
#b = list(map(int,sys.stdin.readline().split()))


mat = []


for i in range(n):
    a[i] = [a[i],i]
    b[i] = [b[i],i]
    
a.sort()
b.sort()



#for i in range(n):
#    if(a[i][1] <= b[i][1]):
#        mat.append([a[i][1],b[i][1]])
#    else:
#        mat.append([b[i][1],a[i][1]])
#        

for i in range(n):
    mat.append([a[i][1],b[i][1]])
        
mat.sort()
print(mat)
        
        

    
    
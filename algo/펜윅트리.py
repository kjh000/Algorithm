# -*- coding: utf-8 -*-
"""
Created on Thu May 16 10:00:22 2019

@author: kjh1
"""

n,m = map(int,input().split())

numb = input()

num = []

for i in range(len(numb)):
    num.append(int(numb[i]))
    
tree = [0]*(n+1)

def update(x,val):
    while(x<=n):
        tree[x] += val
        x +=(x&-x)
        
def query_sum(x):
    
    sumation = 0
    while(x>0):
        sumation += tree[x]
        x -= (x&-x)
        
    return sumation

def range_update(x,y,val):
    if(x<=y):
        update(x,val)
        update(y+1,-val)
    else:
        update(1,val)
        update(x+1,-val)
        update(y,val)



for i in range(n):
    update(i+1,num[i])
print(tree)
print(query_sum(4))



range_update(1,4,1)
print(tree)
print(query_sum(4))
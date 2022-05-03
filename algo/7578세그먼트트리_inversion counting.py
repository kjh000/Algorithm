# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 11:13:51 2019

@author: kjh1
"""
import sys

n = int(input())

a = list(map(int,input().split()))
#a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,input().split()))
#b = list(map(int,sys.stdin.readline().split()))
counting = 0
tree = [0]*(n*4)

order = {}

for i in range(n):
    order[a[i]] = 0

for i in range(n):
    order[b[i]] = i


v = list(order.values())


def update(tree,node,start,end,index,diff):
    
    if(not(start<= index and index <= end)):
        return
    
    tree[node] += diff
    
    if(start != end):
        mid = (start + end)//2
        update(tree,node*2,start,mid,index,diff)
        update(tree,node*2 +1, mid +1,end,index,diff)



def sumation(tree,node,start,end,left,right):
    if(left > end or right < start):
        return 0
    
    if(left <= start and end <= right):
        return tree[node]
    
    mid = (start + end)//2
    
    return sumation(tree,node*2,start,mid,left,right) + sumation(tree,node*2 + 1, mid +1, end,left,right)



for i in range(n):
    if(v[i] == n-1): 
        update(tree,1,0,n-1,v[i],1)
    else:
        update(tree,1,0,n-1,v[i],1)
        a = sumation(tree,1,0,n-1,v[i]+1,n-1)
        counting += a
        
#print(tree)
#print(counting)
print(counting)
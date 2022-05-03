# -*- coding: utf-8 -*-
"""
Created on Mon May 13 15:47:12 2019

@author: kjh1
"""

tree = [None]*14

def init(arr,tree,node,start,end):
    
    if (start == end):
        
        tree[node] = arr[start]

    else:
        mid = (start + end)//2
        
        tree[node] =  init(arr,tree,node*2,start,mid) + init(arr,tree,node*2 +1,mid +1,end)
        
        
    return tree[node]

init([1,1,1,1,1,1,1],tree,1,0,6)

#print(tree)

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
    
print(sumation(tree,1,0,6,0,6))

update(tree,1,0,6,1,2)


print(sumation(tree,1,0,6,0,6))
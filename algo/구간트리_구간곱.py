# -*- coding: utf-8 -*-
"""
Created on Mon May 13 15:47:12 2019

@author: kjh1
"""
MOD = 10**9 + 7
tree = [None]*14
val = 1

def init(arr,tree,node,start,end):
    
    if (start == end):
        
        tree[node] = arr[start]

    else:
        mid = (start + end)//2
        
        tree[node] =  (init(arr,tree,node*2,start,mid)%MOD)*(init(arr,tree,node*2 +1,mid +1,end)%MOD)
        
        
    return tree[node]

init([1,2,3,4,5,6,7],tree,1,0,6)

#print(tree)

def update(tree,node,start,end,index,diff):
    
    if(not(start<= index and index <= end)):
        return tree[node]
    
#    tree[node] += diff
    if start == end:
        return diff
    
    mid = (start + end)//2
    tree[node] = update(tree,node*2,start,mid,index,diff)*update(tree,node*2 +1, mid +1,end,index,diff)
    
    return tree[node]

def mul(tree,node,start,end,left,right):
    if(left > end or right < start):
        return 1
    
    if(left <= start and end <= right):
        return tree[node]
    
    mid = (start + end)//2
    
    return mul(tree,node*2,start,mid,left,right)*mul(tree,node*2 + 1, mid +1, end,left,right)



print(mul(tree,1,0,6,0,6))
update(tree,1,0,6,2,2)
print(mul(tree,1,0,6,0,6))

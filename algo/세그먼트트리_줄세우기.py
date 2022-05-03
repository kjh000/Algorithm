# -*- coding: utf-8 -*-
"""
Created on Mon May 13 15:47:12 2019

@author: kjh1
"""

N = int(input())

tree_o = [None]*(N*4)

ans = [-1]*(N)

def init(arr,tree,node,start,end):
    
    if (start == end):
        
        tree[node] = arr[start]

    else:
        mid = (start + end)//2
        
        tree[node] =  init(arr,tree,node*2,start,mid) + init(arr,tree,node*2 +1,mid +1,end)
        
        
    return tree[node]


def update(tree,node,start,end,index,diff):
    
    if(not(start<= index and index <= end)):
        return
    
    tree[node] += diff
    
    if(start != end):
        mid = (start + end)//2
        update(tree,node*2,start,mid,index,diff)
        update(tree,node*2 +1, mid +1,end,index,diff)


def find(node,tree,s,e,target,idx):
    tree[node] -= 1
    if s == e:
        ans[idx-1] = H[s]
        return
    L,R = node*2,node*2 +1
    mid = (s+e)//2
    if target <= tree[L]:
        find(L,tree,s,mid,target,idx)
    else:
        find(R,tree,mid+1,e,target - tree[L],idx)
    
H = []
for i in range(N):
    a = int(input())
    H.append(a)

order = list(map(int,input().split()))

H.sort()
ones = [1]*N

init(ones,tree_o,1,0,N-1)

for i in range(N):
    now = order.pop()
    find(1,tree_o,0,N-1,now+1,N-i)
    
for i in range(N):
    print(ans[i])
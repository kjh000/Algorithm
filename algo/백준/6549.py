# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 10:07:02 2019

@author: kjh1
"""

INF = 10**9 + 1

def build(a,v,start,end):
    
    if (start == end):
        
        tree[v] = a[start]

    else:
        mid = (start + end)//2
        build(a,v*2, start,mid)
        
        build(a,v*2 + 1,mid+1,end)
        tree[v] = min(tree[2*v],tree[2*v+1])
        
    return tree

def range_minimum_query(node, segx, segy, qx, qy):
    '''
    returns the minimum number in range(qx,qy)
    segx and segy represent the segment index

    '''
    if qx > segy or qy < segx:      # query out of range
        return 10**9 + 7
    elif segx >= qx and segy <= qy:  # query range inside segment range
        return tree[node]
    else:
        return min(range_minimum_query(node*2, segx, (segx + segy)//2, qx, qy), range_minimum_query(node*2 + 1, ((segx + segy)//2) + 1, segy, qx, qy))



mat = list(map(int,input().split()))

tree = [0]*mat[0]*3

box = mat[1:]

square = []


for i in range(len(box)):
    box[i] = [box[i],i+1]


build(box,1,0,mat[0]-1)


a = range_minimum_query(1, 1, mat[0], 1, mat[0])

def dq(arr,qx,qy):
    
    if(qx >= 1 and qy <= mat[0] and qx <= qy):
    
        
        a = range_minimum_query(1,1,mat[0],qx,qy)
    
        square.append(a[0]*(qy-qx+1))
    
            
    
    else:
    
        return
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:09:53 2019

@author: kjh1
"""
import math
#
#n,m,k = map(int,input().split())
#
#logh = math.log2(n)
#h = round(logh + 0.5)
#tree_size = 2**h
#
#numbers = []
#query = []

#tree = [-1]*(2*tree_size)


#for i in range(n):
#    
#    numbers.append(int(input()))
    
#for i in range(n+k):
#    
#    query.append(list(map(int,input().split())))
#    
#tree = [None]*14

#tree = [None]*8

tree = [0]*18

def build(a,v,start,end):
    
    if (start == end):
         
        tree[v] = a[start]

    else:
        mid = (start + end)//2
        build(a,v*2, start,mid)
        
        build(a,v*2 + 1,mid+1,end)
        tree[v] = min(tree[2*v],tree[2*v+1])
        
    return tree

#build([18,17,13,19,15,11,20],1,0,6)
#build([5,4,3,2,1,6],1,0,5)
build([6,5,4,3,2,1],1,0,5)
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

#print (range_minimum_query(1, 1, 7, 1, 3))
#print(tree)
a = range_minimum_query(1, 1, 6, 1, 4)
print(a)
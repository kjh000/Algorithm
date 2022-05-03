# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:44:30 2019

@author: kjh1
"""

#n = int(input())
n = 5
tree = [[None,0] for i in range(3*n)] ## [value,lazy]
arr = [0,0,0,0,0]
tree[0] = [None,None]

def init(node,start, end):
    if(start == end):
        tree[node][0] = arr[start]
        
    
    else:
        tree[node][0] = init(node*2,start,(start+end)//2) + init(node*2 +1,(start + end)//2 + 1,end)

    
    return tree[node][0]





def build(a,v,start,end):
    
    if (start == end):
        
        tree[v][0] = a[start]

    else:
        mid = (start + end)//2
        build(a,v*2, start,mid)
        
        build(a,v*2 + 1,mid+1,end)
        tree[v][0] = min(tree[2*v][0],tree[2*v+1][0])
        
    return tree





def update_range(node,start,end,i,j,diff):
    
    if(tree[node][1] != 0):
        tree[node][0] += (end - start +1)*tree[node][1]
        if(start != end):
            tree[node*2][1] += tree[node][1]
            tree[node*2 +1][1] += tree[node][1]
            
            
        tree[node][1] = 0
    
    if(j < start or i > end):  return
    
    if(i <= start and end<= j):
        tree[node][0] += (end - start +1)*diff
        if(start != end):
            tree[node*2][1] += diff
            tree[node*2 +1][1] += diff

        return

    update_range(node*2,start,(start+end)//2,i,j,diff)

    update_range(node*2 + 1,(start+end)//2 + 1,end,i,j,diff)

    tree[node][0] = tree[node*2][0] + tree[node*2 +1][0]
    
def sumation(node,start,end,i,j):
    if(tree[node][1] != 0):
        tree[node][0] += (end - start +1)*tree[node][1]
        if(start != end):
            tree[node*2][1] += tree[node][1]
            tree[node*2 +1][1] += tree[node][1]
            
        tree[node][1] =0


    if(i>end or j < start): return 0
    if(i <= start and end <= j):    return tree[node][0]
    
    return sumation(node*2,start,(start+end)//2,i,j) + sumation(node*2 +1,(start+end)//2 + 1 ,end,i,j)



def range_minimum_query(node, segx, segy, qx, qy):
    '''
    returns the minimum number in range(qx,qy)
    segx and segy represent the segment index

    '''
    if qx > segy or qy < segx:      # query out of range
        return 10**9 + 7
    elif segx >= qx and segy <= qy:  # query range inside segment range
        return tree[node][0]
    else:
        return min(range_minimum_query(node*2, segx, (segx + segy)//2, qx, qy), range_minimum_query(node*2 + 1, ((segx + segy)//2) + 1, segy, qx, qy))


    

init(1,0,n-1)
update_range(1,1,5,1,5,1)

print(sumation(1,1,5,1,5))

update_range(1,1,5,1,1,1)

print(sumation(1,1,5,1,5))


update_range(1,1,5,1,5,1)

print(sumation(1,1,5,1,1))

#print(tree)

update_range(1,1,5,1,1,1)

print(sumation(1,1,5,1,1))
#
#print(sumation(1,1,5,1,2))








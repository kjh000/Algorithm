# -*- coding: utf-8 -*-
"""
Created on Thu May 23 12:10:09 2019

@author: kjh1
"""

import sys


def init(node,start, end):
        if(start == end):
            tree[node][0] = arr[start]
            
        
        else:
            tree[node][0] = init(node*2,start,(start+end)//2) + init(node*2 +1,(start + end)//2 + 1,end)
    
        
        return tree[node][0]
    
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

T = int(input())

for t in range(T):
    
    n,q = map(int,input().split())
    
#    n,q = map(int,sys.stdin.readline().split())
    
    lr = []
    arr = [0]*n
    tree = [[None,0] for i in range(3*n)]
    
    book = []
    
    for i in range(q):
        l,r = map(int,input().split())
        
#        l,r = map(int,sys.stdin.readline().split())
        
        lr.append([r-l+1,l,r])
        
    lr.sort()
        
    
    init(1,0,n-1)
    
    
    for i in range(q):
        
        cover =lr[i][0] - sumation(1,1,n,lr[i][1],lr[i][2])
    
        book.append(cover)
        if(i>0):
            if(lr[i][1]<=lr[i-1][1] and lr[i][2] >= lr[i-1][2]):
                update_range(1,1,n,lr[i-1][1],lr[i-1][2],-1)
            elif(lr[i][1]>=lr[i-1][1] and lr[i][2] >= lr[i-1][2]):
                update_range(1,1,n,lr[i][1],lr[i-1][2],-1)
            elif(lr[i][1]<=lr[i-1][1] and lr[i][2] <= lr[i-1][2]):
                update_range(1,1,n,lr[i-1][1],lr[i][2],-1)
        update_range(1,1,n,lr[i][1],lr[i][2],1)
        
    ans = min(book)
    print('Case #{}: {}'.format(t+1,ans))
#    sys.stdout.write('Case{}: {}'.format(t+1,ans))
#    
#    sys.stdout.write('\n')

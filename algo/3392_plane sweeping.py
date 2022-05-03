# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 16:54:09 2019

@author: kjh1
"""
import sys
MAX_Y = 30000
MAX_N = 10000
n = int(input())

mat = []
arr = [[] for _ in range(2*MAX_N)]
seg = [0]*(4*MAX_Y)
cnt = [0]*(4*MAX_Y)
res = 0
last = 0


def update(lo,hi,val,node,x,y):
    if(y<lo or hi <x): return
    
    if(lo <= x and y<= hi):
        cnt[node] += val
    
    else:
        mid = (x+y)//2
        update(lo,hi,val,node*2,x,mid)
        update(lo,hi,val,node*2 +1,mid +1,y)
        
    if(cnt[node] > 0):
        seg[node] = y - x + 1
    else:
        if(x==y): seg[node] = 0
        else:
            seg[node] = seg[node*2] + seg[node*2 + 1]
            
            
for i in range(n):
#    x1,y1,x2,y2 = map(int,input().split())
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    arr[i] = [x1,y1,y2-1,1]
    arr[i+n] = [x2,y1,y2-1,-1]
    
arr = arr[:2*n]
arr.sort()

for i in range(2*n):
    
    if(i):
        dx = arr[i][0] - last
        res += dx*seg[1]
        
    update(arr[i][1],arr[i][2],arr[i][3],1,0,MAX_Y)
    last = arr[i][0]        
    
print(res)

#print(arr)
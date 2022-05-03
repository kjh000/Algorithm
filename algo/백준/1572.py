# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 13:36:23 2019

@author: kjh1
"""
import sys

n,k = map(int,input().split())

mat = []

for i in range(n):
#    m = int(input())
    m = int(sys.stdin.readline())
    mat.append(m)
    
arr = mat[:k]
arr.sort()
ans = 0

center = (k-1)//2

def binary_del(start,end,target):
    mid = (start + end)//2
    
    if(arr[mid] == target):
        del arr[mid]
        return
    else:
        if(arr[mid]>target):
            binary_del(start,mid,target)
        else:
            binary_del(mid+1,end,target)
            

def binary_insert(start,end,target):
    mid = (start + end)//2
    
    if(arr[start] >= target):
        arr.insert(start,target)
        return
    elif(arr[end]<= target):
        arr.insert(end+1,target)
        return
    elif(arr[mid]<= target and arr[mid+1] >= target):
        arr.insert(mid+1,target)
    else:
        if(arr[mid]>target):
            binary_insert(start,mid,target)
        else:
            binary_insert(mid+1,end,target)
        
if(n == 0 or k == 0):
    print(0)
elif(k == 1):
    print(sum(mat))
else:
    for i in range(k-1,n):
    
        if(i < n-1):
            ans += arr[center]
           
            binary_del(0,k-1,mat[i-k+1])
            
            binary_insert(0,k-2,mat[i+1])
            
        else:
            ans += arr[center]
            
    print(ans)

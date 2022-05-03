# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:20:08 2019

@author: kjh1
"""



n = int(input())

mat = list(map(int,input().split()))

m = int(input())

nums = list(map(int,input().split()))

ans = []

mat.sort()

def bin_search(start,end,a):
    
    mid = (end + start)//2
    
    if(mat[mid] == nums[a]):
        ans.append(1)

    elif(end - start == 0):
        
        ans.append(0)
        
    else:
        
        if(mat[mid] > nums[a]):
            
            bin_search(start,mid,a)
        else:
            bin_search(mid+1,end,a)
            

for i in range(m):
    bin_search(0,n-1,i)

    print(ans[i])

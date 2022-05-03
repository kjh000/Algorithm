# -*- coding: utf-8 -*-
"""
Created on Fri May 24 15:36:42 2019

@author: kjh1
"""
import sys

def binary_search(target,arr):
    
    start = 0 
    end = len(arr) - 1
    
    while(start <= end):
        
        mid = (start + end)//2
        
        if(arr[mid] == target):
            return '1'
        
        elif(arr[mid] < target):
            start = mid + 1
        else:
            end = mid -1
            
    return '0'


n = int(input())

#arr1 =list(map(int,input().split()))

arr1 = list(map(int,sys.stdin.readline().split()))

arr1.sort()

m = int(input())

#arr2 = list(map(int,input().split()))


arr2 = list(map(int,sys.stdin.readline().split()))
ans = []

for i in range(m):
    
#    print(binary_search(arr2[i],arr1),end=' ',flush = True)
    
    sys.stdout.write(binary_search(arr2[i],arr1))
    
    sys.stdout.write(' ')


    

    


# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 16:19:59 2020

@author: kjh1
"""
'''''
if key in list : return index
if key not in list : return insertion point (minus)
'''''
def binary_search(lst,key):
    low = 0
    high = len(lst) - 1
    
    
    while high >= low:
        mid = (low + high)//2
        if key < lst[mid]:
            high = mid -1
        elif key == lst[mid]:
            return mid
        else:
            low = mid + 1
            
    return -low -1
    
mat = [1,2,2,2,3,4]

a = binary_search(mat,2)

print(a)
print(mat)

#mat.insert(-a-1,3)
#mat.insert(a,2)
#print(mat)
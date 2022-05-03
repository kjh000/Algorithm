# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 14:36:06 2019

@author: kjh1

"""

MIN = -2 ** 31 - 1

def divide_conquer(arr):
    N = len(arr)

    def find(lo, hi):
        # 1.
        if lo == hi:
            return arr[lo]

        mid = (lo + hi) // 2
	 
        left = find(lo, mid)
        right = find(mid+1, hi)

        
        tmp = 0
        left_part = MIN
        for i in range(mid, lo-1, -1):
            tmp += arr[i]
            left_part = max(left_part, tmp)

        tmp = 0
        right_part = MIN
        for i in range(mid+1, hi+1):
            tmp += arr[i]
            right_part = max(right_part, tmp)

        
        return max(left, right, left_part + right_part)

    
    return find(0, N-1)


a = [-1,3,-1,5]

print(divide_conquer(a))
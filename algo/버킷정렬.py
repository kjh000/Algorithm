# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 11:19:56 2020

@author: kjh1
"""


def bucket_sort(seq):
    buckets = [[] for _ in range(len(seq))]
    
    for value in seq:
        bucket_index = value*len(seq) // (max(seq) + 1)
        buckets[bucket_index].append(value)
        
    sorted_list = []
    for bucket in buckets:
        sorted_list.extend(quick_sort(bucket))
        
    return sorted_list

def quick_sort(ARRAY):
    ARRAY_LENGTH = len(ARRAY)
    if ARRAY_LENGTH <= 1 :
        return ARRAY
    else:
        PIVOT = ARRAY[0]
        GREATER = [element for element in ARRAY[1:] if element > PIVOT]
        LESSER = [element for element in ARRAY[1:] if element <= PIVOT]
        
        return quick_sort(LESSER) + [PIVOT] + quick_sort(GREATER)
    
    
#a = [0.78,0.17,0.39,0.26,0.72,0.94,0.21,0.12,0.23,0.68]
a = [29,25,3,49,9,37,21,43]

b = bucket_sort(a)

print(b)
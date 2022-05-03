# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 13:34:46 2019

@author: kjh1
"""
import sys

sys.setrecursionlimit(10**6)

def findCandidates( priceList, selectedList,  m):    
    global candidates
    if sum(selectedList) > m:
        return
    elif sum(selectedList) == m:
        candidates.append(selectedList)
        return
        
    for price in priceList:
        findCandidates(priceList, selectedList+[price], m)
        
while True:
#    n, m = map(float, sys.stdin.readline().split())
    n, m = map(float, input().split())
    n = int(n)
    if n == 0:
        break    
        
    items = {}
    for _ in range(n):
        c, p = map(float, input().split())
        c = int(c)
        items[p] = c

    candidates = []    
    findCandidates(items.keys(), [], m)
    cals = []
    for candidate in candidates:
        cal = 0
        for price in candidate:
            cal += items[price]
        cals.append(cal)
#    print(n, m, cals)
    print(max(cals))
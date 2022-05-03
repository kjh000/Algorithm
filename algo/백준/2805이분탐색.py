# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:25:22 2019

@author: kjh1
"""

n,m = map(int,input().split())

trees = list(map(int,input().split()))


l,h = 0, max(trees)

while l<h:
    mid = (l + h)//2
#    print(mid)
    
    total = 0
    start,end  = l,h
    for i in range(n):
        if(trees[i]>mid):
            total += (trees[i] - mid)
            
    if(total == m):
        break
    elif(total < m):
        h = mid
    elif(total > m):
        if(mid == end-1):
            break

        else:
            l = mid
            
print(mid)
            
#            
#
#def search_tree(start,end):
#    
#    mid = (start+end)//2
#    total = 0
#    
#    for i in range(n):
#        if(mid < trees[i]):
#            total += (trees[i] - mid)
#            
#    if(total == m):
#        
#        print(mid)
#        
#
#    
#    else:
#        
#        if(total > m):
#            if(end == mid + 1 or start == end):
#                
#                print(mid)
#                
#            
#            else:
#                search_tree(mid+1,end)
#            
#        elif(total < m):
#            search_tree(start,mid)
#        
#        
#            
#search_tree(0,trees[-1])
#
#            
            
            
            
            
            
            
            
            
            
            
            
            
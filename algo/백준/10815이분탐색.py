# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:16:49 2019

@author: kjh1
"""

n = int(input())

cards = list(map(int,input().split()))

m = int(input())

mat = list(map(int,input().split()))

cards.sort()

ans = []


def bin_search(start,end,a):
    
    mid = (end + start)//2
    
    if(cards[mid] == mat[a]):
        ans.append(1)

    elif(end - start == 0):
        
        ans.append(0)
        
    else:
        
        if(cards[mid] > mat[a]):
            
            bin_search(start,mid,a)
        else:
            bin_search(mid+1,end,a)
            

for i in range(m):
    bin_search(0,n-1,i)

    print(ans[i],end = ' ')

# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 13:27:19 2019

@author: kjh1
"""

nk = list(map(int,input().split()))
n = nk[0]
k = nk[1]
moves = 0

while(n != k):
    
    if(n>k):
        n -= 1
#        print(n)
        moves +=1
        
    elif(2*n <= k):
        n = 2*n
        print(n)
        moves +=1 
    elif(2*n - k <= 1):
        n = 2*n
#        print(n)
        moves += 1
    elif(2*n - k >= 2):
        n -= 1
#        print(n)
        moves += 1

print(moves)        

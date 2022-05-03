# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 10:53:50 2019

@author: kjh1
"""

T = int(input())

for t in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    count = 0
    A.sort()
    
    if(A.count(0)>1):
        count += ((A.count(0)*(A.count(0)-1))//2)*(len(A)-A.count(0))
 
    
    for i in range(N-2):
                                    
        for j in range(i+1,N-1):
            
            if(A[i]*A[j]>A[-1]):
                break
            else:
                if(A[i]*A[j] in A[j+1:]):
                    count += A[j+1:].count(A[i]*A[j])

                    
                    
    print('Case #{}: {}'.format(t+1,count))
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 17:28:36 2019

@author: kjh1
"""

T = int(input())
for t in range(T):
    n= int(input())
    
    a = n
    
    mat = []
    count = 0
    k = 0
    numbers = [0]*10001
    for i in range(1,101):
        mat.append(i**2)
    
    mat.reverse()
    
    for i in range(1,101):
        numbers[i**2] = 1

    
    for l in range(2,6):
        for i in range(1,101):
            if((i**2)*l <= 10000):
                if(numbers[(i**2)*l] == 0):
                   numbers[(i**2)*l] = l
    
    while(n != 0):
        
        if(n>=mat[k]):
            n -= mat[k]
            count += 1
        else:
            k += 1
    
        
    if(numbers[a] != 0):
        ans = min(count,numbers[a])
    else:
        ans = count
    
    
    
#    print(numbers[n+1],count)
    print('Case #{}: {}'.format(t+1,ans))
#    print('{} -> {}'.format(a,ans))

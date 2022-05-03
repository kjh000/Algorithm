# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:57:57 2019

@author: kjh1
"""

T = int(input())
for t in range(T):
    n = int(input())
    ans = 0
    numbers = list(map(int,input().split()))
    s = 1
    
    if(len(numbers)<=2):
        print('Case #{}: YES'.format(t+1))
        
    else:
        while(True):
            
            if(len(numbers)==2):
                break
                        
            if(len(numbers)%2 == 0 ):
                long = (len(numbers)//2)-1
            else:
                long = len(numbers)//2
                
            if(numbers[long] == n):
                n -= 1
                del numbers[long]
            elif(numbers[long] == s):
                s += 1
                del numbers[long]
               
            else:
        
                break
            
        if(len(numbers) == 2):
            print('Case #{}: YES'.format(t+1))
        else:
            print('Case #{}: NO'.format(t+1))                  
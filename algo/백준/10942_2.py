# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 16:10:00 2019

@author: kjh1
"""

N = int(input())

numbers = list(input().split())
numbers = list(map(int,numbers))
numbers.insert(0,0)
Q = int(input())

dp_arr = [0]*Q

for i in range(Q):
    se = list(input().split())
    se = list(map(int,se))
    
    if(Q>1):
        dp_arr[i] = numbers[se[0]:se[1]+1]
    else:
        dp_arr[i] = [0]
    


def isP(i):
    
    
    if(len(dp_arr[i]) == 1):
        print(1)  
    else:
        if(len(dp_arr[i]) == 2):
            if(dp_arr[i][0] == dp_arr[i][1]):
                print(1)
            else:
                print(0)
        elif(dp_arr[i][0] == dp_arr[i][-1]):
            del dp_arr[i][0]
            del dp_arr[i][-1]
            isP(i)
        
        else:
            print(0)
            

for i in range(Q):
    isP(i)
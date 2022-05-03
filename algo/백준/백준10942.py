# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 09:46:56 2019

@author: kjh1
"""

import sys

#sys.stdin.readline()

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
        print(0)
    


def isP(i):
    if(Q>0):
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
########################################
#
#N = int(input())
#
#numbers = list(input().split())
#numbers = list(map(int,numbers))
#numbers.insert(0,0)
#Q = int(input())
#
#dp_arr = [0]*Q
#
#
#
#for i in range(Q):
#    se = list(input().split())
#    se = list(map(int,se))
#    
#    dp_arr[i] = numbers[se[0]:se[1]+1]
#    
#    
#
#
#def isP(i):
#    
#    if(len(dp_arr[i]) == 1):
#        print(1)  
#    else:
#        if(len(dp_arr[i]) == 2):
#            if(dp_arr[i][0] == dp_arr[i][1]):
#                print(1)
#            else:
#                print(0)
#        elif(dp_arr[i][0] == dp_arr[i][-1]):
#            del dp_arr[i][0]
#            del dp_arr[i][-1]
#            isP(i)
#        
#        else:
#            print(0)
#            
#
#for i in range(Q):
#    isP(i)

#def isP2(i):
#   
#    if(len(dp) == 1):
#            dp_arr[i] = 1
#            return 
#    else:
#        if(len(dp) == 2):
#            if(dp[0] == dp[1]):
#                    dp_arr[i] =1
#                    return 
#            else:
#                    dp_arr[i] = 0
#                    return 
#        elif(dp[0] == dp[-1]):
#            del dp[0]
#            del dp[-1]
#            isP2(i)
#            
#        else:
#            dp_arr[i] = 0
#            return 
#                
#for i in range(Q):
#   
#    se = list(input().split())
#    se = list(map(int,se))
#    dp = numbers[se[0]:se[1]+1]
#   
#    isP2(i)
#                    
#for i in range(Q):
#    print(dp_arr[i])
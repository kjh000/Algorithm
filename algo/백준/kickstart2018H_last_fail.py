# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 13:43:19 2019

@author: kjh1
"""
#memo = [[[0 for col in range(2*NM[0])] for row in range(2*NM[0])] for depth in range(2*NM[0])]

T= int(input())
modulo = 1000000007
ans = [[0] for i in range(T)]


def f(x,y,z):
    
    
    if(x<0 or y<0):
        return 0
    
    elif(x ==0 and y ==0):
        return 1
    
    else:
        if(z==0):
            if(y>0):
                return x*f(x-1,y,0) + 2*y*f(x+1,y-1,1)
            else:
                return x*f(x-1,0,0)
        else:
            if(y>0):
                return (x-1)*f(x-1,y,0) +2*y*f(x+1,y-1,1)
            else:
                return (x-1)*f(x-1,0,0)
        
#print(f(x,y,0))

for i in range(T):
    
    NM = list(map(int,input().split()))
    
#    memo = [[[0 for col in range(2*NM[0])] for row in range(2*NM[0])] for depth in range(2*NM[0])]

    y = NM[1]
    x = 2*NM[0]-2*y

    ans[i] = f(x,y,0)%modulo

    



for i in range(T):
          
    print("Case #{}: {}".format(i+1,ans[i]))
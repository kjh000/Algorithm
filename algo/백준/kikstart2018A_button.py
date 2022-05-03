# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 17:23:19 2019

@author: kjh1
"""

T = int(input())
ans = [[0] for k in range(T)]

def f(N):
    
    
    eight = ""
    
    
    push = 0
    
    for i in range(len(N)):
        
        if(len(N)!=1 and i == len(N)-1):
            
            if(int(N[i])%2 == 0):
                return 0
            else: return 1
        
        if(len(N) == 1):
            if(int(N[i])%2 == 0):
                push = 0
                return push
            else:
                if(int(N[i])<5):
                    push = 1
                    return push
                else:   return 1
        else:
            if(int(N[i])%2 == 0):
                continue
            else:
                if(int(N[i]) == 9):
                    
                        eight += '8'
                        for j in range(len(N[i+1:])):
                            eight += '8'
                        push = int(N[i:]) - int(eight)
                        return push

                else:
                    if(int(N[i+1])>=5):
                        push = 10**(len(N[i+1:])) - int(N[i+1:])
                        return push
                    else:
                        if(len(N)>=3 and N[i+1]=='4' and int(N[i+2])>=5):
                            
                            push = 10**(len(N[i+1:])) - int(N[i+1:])
                            return push                            
                            
                            
                        else:    
                            eight += str(int(N[i])-1)
                            for j in range(len(N[i+1:])):
                                eight += '8'
                            push = int(N[i:]) - int(eight)
                            return push


for i in range(T):
    
    n = input()
    n = int(n)
    n = str(n)
    ans[i] = f(n)

        



for i in range(T):
    
    print("Case #{}: {}".format(i+1,ans[i]))

          
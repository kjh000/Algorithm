# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 10:24:15 2019

@author: kjh1
"""
import sys

T = int(sys.stdin.readline())

for t in range(T):
    a,b = sys.stdin.readline().split()
#    ab = input()
    
    N = int(sys.stdin.readline())
#    ans = int(ab.split()[1])
    ans = int(b)
    big = [0]
    small=[0]
    for i in range(N):
        
        print(ans)
        sys.stdout.flush()
            
            
        s = sys.stdin.readline().rstrip()
        if(s == 'CORRECT'):
            break
        elif(s == 'TOO_BIG'):
                
            big.append(ans)
            ans = (ans+small[-1])//2

                
        elif(s == 'TOO_SMALL'):
            ans = (big[-1]+ans)//2
            if(ans == small[-1]):
                ans += 1
                small.append(ans)
            else:
                small.append(ans)
            
            
        else:
            sys.exit()
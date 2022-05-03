# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 15:02:34 2019

@author: kjh1
"""

letters = 'abcdefghijklmnopqrstuvwxyz'

T = int(input())
for t in range(T):
    lnk = list(map(int,input().split()))
    ans = 0
    
    p= lnk[0]
    sump = p
    
    for i in range(1,lnk[1]):
        if((i+1)%2 == 0):
            p = p
            sump += p
    #        print(p)
        else:
            p = p*lnk[0]
            sump += p
    #        print(p)
    
    line = sump//lnk[0]
    #print(sump)
    #print(line)
    k = lnk[1]
    if(lnk[2]>sump):
        ans = 0
    else:
        if(lnk[2]<=line):
    #            lnk[2] = lnk[2]%line
            if(lnk[2]<=lnk[1]):
                ans = lnk[2]
            else:
                
                for i in range(3,lnk[1]+1):
                    if(i%2 == 1):
                        if(k-lnk[0]**(i-2) <= lnk[0]**(i-2)):
                            ans = i
                            break
                        else:
                            k -= lnk[0]**(i-2)
                    else:
                        if(k-lnk[0]**(i-3)<=lnk[0]**(i-3)):
                            ans = i
                            break
                        else:
                            k -= lnk[0]**(i-3)
        else:
            num = lnk[2]//line
            lnk[2] = lnk[2]%line
            
    print('Case #{}: {}'.format(t+1,ans))
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 09:52:31 2019

@author: kjh1
"""

T = int(input())

nod = list(map(int,input().split()))
line = list(map(int,input().split()))
"""
x1,x2,a,b,c,m,l
"""
x = 0
x1 = 0
x2 = 0
s = 0
o = 0
total = 0
maxi = 0
i = 0

for i in range(nod[0]):
    if(i == 0):
        x = line[0]
        s = x + line[6]
        x1 = x
        
        if(s<=nod[2]):
            total += s
            maxi = s
            i += 1
            if(s%2 == 1):
                o += 1
    elif(i == 1):
        x = line[1]
        s = x + line[6]
        x2 = x1
        x1 = x
        
        if(s%2 == 0):
            total += s
            if(total<=nod[2]):
                maxi = total
                i += 1
            else:
                if(s >= total-s):
                    total = s
                    maxi = s
                    i += 1
                else:
                    maxi = total-s
                    total = 0
                    i += 1
        else:
            if(o<nod[1]):
                
                total += s
                
                if(total<=nod[2]):
                    maxi = total
                    o += 1
                    i += 1
                else:
                    if(s >= total-s):
                        total = s
                        maxi = s
                        o = 1
                        i += 1
                    else:
                        maxi = total-s
                        total = 0
                        o = 0
                        i += 1
            else:
                if(s>= total):
                    total = s
                    maxi = s
                    o = 1
                    i += 1
                else:
                    maxi = total
                    total =0
                    o = 0
                    i += 1
    else:
        x = (line[2]*x1 + line[3]*x2 + line[4])%line[5]
        x2 = x1
        x1 = x
        s = x + line[6]
        print(s)
        
        if(s%2 == 0):
            total += s
            if(total<=nod[2]):
                maxi = total
                i += 1
            else:
                if(s >= total-s):
                    total = s
                    maxi = s
                    i += 1
                else:
                    maxi = total-s
                    total = 0
                    i += 1
        else:
            if(o<nod[1]):
                
                total += s
                
                if(total<=nod[2]):
                    maxi = total
                    o += 1
                    i += 1
                else:
                    if(s >= total-s):
                        total = s
                        maxi = s
                        o = 1
                    else:
                        maxi = total-s
                        total = 0
                        o = 0
                        i += 1
            else:
                if(s>= total):
                    total = s
                    maxi = s
                    o = 1
                    i += 1
                else:
                    maxi = total
                    total =0
                    o = 0
                    i += 1
                    
print(maxi)
            
                
    
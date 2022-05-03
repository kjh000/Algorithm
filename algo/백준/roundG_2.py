# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 14:56:16 2019

@author: kjh1
"""

T = int(input())

for t in range(T):
    NQ= list(map(int,input().split()))
    xline = list(map(int,input().split()))
    yline = list(map(int,input().split()))
    zline = list(map(int,input().split()))
    
    x = []
    y = []
    z = []
    l = []
    r = []
    k = []
    ans = 0
    
    scores = []
    
    for i in range(NQ[0]):
        if(i < 2):
            x.append(xline[i])
            y.append(yline[i])
            l.append(min(x[i],y[i])+1)
            r.append(max(x[i],y[i])+1)
        else:
            x.append((xline[2]*x[i-1]+xline[3]*x[i-2]+xline[4])%xline[5])
            y.append((yline[2]*y[i-1]+yline[3]*y[i-2]+yline[4])%yline[5])
            l.append(min(x[i],y[i])+1)
            r.append(max(x[i],y[i])+1)
            
            
            
    for i in range(NQ[1]):
        if(i <2 ):
            z.append(zline[i])
            k.append(z[i]+1)
        else:
            z.append((zline[2]*z[i-1]+zline[3]*z[i-2]+zline[4])%zline[5])
            k.append(z[i]+1)





            
    for i in range(NQ[0]):
        for j in range(l[i],r[i]+1):
            scores = scores + [j]
            
    scores.sort(reverse = True)
    
    for i in range(1,NQ[1]+1):
        if(k[i-1]>len(scores)):
            ans += 0
            
        else:
            ans += i*scores[(k[i-1])-1]
           
        
    
    print('Case #{}: {}'.format(t+1,ans))
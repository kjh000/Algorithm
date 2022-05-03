# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 15:31:10 2019

@author: kjh1
"""

T = int(input())
for t in range(T):
    NMP = list(map(int,input().split()))
    p = []
    m=[]
    op = [0]*NMP[2]
    choose = 0b0
    ans = 0
    
    for i in range(NMP[0]):
        p.append(input())
        for j in range(NMP[2]):
            if(p[i][j] == '1'):
                op[j] += 1
                
    op.reverse()
    op1 = op[:]
    
    for i in range(NMP[1]):
        m.append(input())
        
    for i in range(NMP[2]):
        if(op[i]>NMP[0]//2):
            choose |= (1<<i)
            op1[i]=0
    
    
    cc = str(bin(choose)[2:])
    
       
    for i in range(NMP[2]):
        if(cc in m):
            if(op1[i] == max(op1)):
                choose ^= (1<<i)
                op1[i] = 0
                break
            
    op.reverse()
        
    c1 = str(bin(choose)[2:])
    
    
    for i in range(len(c1)):
        if(c1[i]=='1'):
            ans += NMP[0] - int(op[i])
        else:
            ans += int(op[i])
    
    print('Case #{}: {}'.format(t+1,ans))
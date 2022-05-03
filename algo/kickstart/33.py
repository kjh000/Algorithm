# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 16:33:48 2019

@author: kjh1
"""

T = int(input())

BIG = (10**9)+7

for t in range(T):
    
    data = list(map(int,input().split()))
    
    x,y = data[2],data[3]
    xx,yy = data[2],data[3]
    
    ai = []
    subb = 0
    power = 0
    
    ai.append((x+y)%data[8])
    
    for i in range(1,data[0]):
        
        x = (data[4]*xx + data[5]*yy + data[6])%data[8]%BIG
        y = (data[5]*xx + data[4]*yy + data[7])%data[8]%BIG
        
        ai.append((x+y)%data[8]%BIG)
        
        xx = x
        yy = y
        
    for i in range(len(ai)):
        
    
        for j in range(len((ai))-i):
    

            subb = ai[j:j+i+1]
            
#            for q in range(data[1]):
#                for w in range(len(subb)):
#                    
#                    power += (subb[w]*((w+1)**(q+1)))%BIG
            
#    
    
    
    
    print('Case #{}: {}'.format(t+1,power%BIG))
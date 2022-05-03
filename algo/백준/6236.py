# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 13:19:11 2019

@author: kjh1
"""

n,m = map(int,input().split())

money = []

right = 0

total = 0
do = 0


for i in range(n):
    
    money.append(int(input()))
    
    right += money[i]
    
left = min(money)

mid = ( right + left )//2


while(True):
    
    for i in range(n):
        
        if(mid < money[i]):
            total = 0
            break
        
        elie:
            
            total += money[i]
            
            if(total  )
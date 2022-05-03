# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 11:04:17 2019

@author: kjh1
"""

def is_Prime(n):
    if(n<2):
        return False
    
    x = int (n**(0.5)) + 1
    
    for i in range(2,x+1):
        if(n%i == 0):
            return False
        
    return True


palindrome = {}

odd = [5,7,9,11,33,55,77,99]

aa,bb = map(int,input().split())


for i in range(1,10):
    palindrome[i] = []
    
    if(i>2):
        palindrome[i].append(10**(i-1) + 1)
   
    

for i in range(1,10):
    palindrome[1].append(i)
    

for i in range(1,10):
    
    palindrome[2].append(11*i)
        
for i in range(3,10):
    
    for j in range(len(palindrome[i-2])):
        
        for k in range(1,10):
             
            a = palindrome[i-2][j]
            
            palindrome[i].append(a*10 + k + k*(10**(i-1)))
            
            if(k%2 == 1):
                odd.append(a*10 + k + k*(10**(i-1)))
odd.sort()
#
#for i in odd:
#    if( i >= aa):
#            
#        if( i > bb):
#            print(-1)
#            break
#        
#        else:
#            if is_Prime(i):
#                print(i)
#

print(palindrome[6])
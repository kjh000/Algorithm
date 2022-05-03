# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 16:11:37 2020

@author: kjh1
"""
import sys

MOD = 10**9 + 7

def binary_search(lst,key):
    low = 0
    high = len(lst) - 1
    
    
    while high >= low:
        mid = (low + high)//2
        if key < lst[mid]:
            high = mid -1
        elif key == lst[mid]:
            return mid
        else:
            low = mid + 1
            
    return -low - 1

N = 200200
tadd = [0]*(N+1)
tmul = [0]*(N+1)

mat = []
def inupadate(at,mul,add):
    if(at<1 or at>N): return
        
    while(at<=N):
        tmul[at] += mul
        tadd[at] += add
        
        at += at&-at
        
def range_update(l,r,by):
    inupadate(l,by,-by*(l-1))
    inupadate(r+1,-by,by*r)
    
def range_query(at):
    if(at==0): return 0
    if(at<1 or at>N): return 
    
    mul,add = 0,0
    
    i = at
    while i>0:
        mul +=tmul[i]
        add += tadd[i]
        i -= i&-i

    return at*mul + add

n = int(input())
ans = 1

for i in range(n):
    x = int(input())
    
    idx = binary_search(mat,x)
    if(i == 0):
        mat.append(x)
        range_update(x+1,x+1,x)
        continue
    if(idx < 0):
        idx = -idx
        if(idx >= i + 1):
            left = range_query(x)
            tmp = x*i - left
            ans = ans*tmp
            mat.append(x)
            
            range_update(x+1,x+1,x)
            
        else:
            left = range_query(x)
            right = range_query(mat[-1]+1) - left
            tmp = x*(idx-1) - left + right - x*(i-idx + 1)
            ans = ans*tmp
            mat.insert(idx-1,x)
            range_update(x+1,x+1,x)
            
            
    else:
        
        if(x == mat[-1]):
            left = range_query(x+1)
            tmp =  x*i - left
            ans = ans*tmp
            mat.append(x)

            range_update(x+1,x+1,x)
        else:
            left = range_query(x+1)
            right = range_query(mat[-1] + 1) -left
            tmp = x*(idx+1) - left + right - x*(i-idx-1)
            ans = ans*tmp
            mat.insert(idx,x)
            range_update(x+1,x+1,x)            
            
    ans = ans%MOD
            
        
print(ans%MOD)
            
        
        
        
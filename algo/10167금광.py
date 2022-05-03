# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 11:29:36 2019

@author: kjh1
"""
import sys
n = int(input())

mat = []
ans = []

def max_sum_dp(dp,arr,n):
    dp[0] = arr[0]
    for i in range(1,n):
        dp[i] = max((dp[i-1]) + arr[i],arr[i])
        
    return(max(dp))

x_order = []
y_order = []

yy = {}
x_index= {}

for i in range(n):
    x,y,w = map(int,input().split())
#    x,y,w = map(int,sys.stdin.readline.split())
    
    mat.append([y,x,w])
    x_order.append(x)
    y_order.append(y)
    
x_order.sort()
y_order.sort()
xx = list(set(x_order))
yz = list(set(y_order))
ly = len(yz)
for i , num in enumerate(xx):
    x_index[num] = i
    
for i in yz:
    yy[i] = []
    


for i in range(n):
    yy[mat[i][0]].append([x_index[mat[i][1]],mat[i][2]])
    

for t in range(ly):
    dp = [0]*(len(xx))
    arr = [0]*(len(xx))
    for i in range(t,ly):
        
        for j in range(len(yy[yz[i]])):
            arr[yy[yz[i]][j][0]] += yy[yz[i]][j][1]
        
        aa = max_sum_dp(dp,arr,len(xx))
        
        ans.append(aa)
    
print(max(ans))
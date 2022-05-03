# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:02:19 2019

@author: kjh1
"""

T = int(input())

n,Ts,Tf = map(int,input().split())

current = 0
ss = 0


minimum = [0]*(n-1)

sfd = [[None]*3 for i in range(n-1)]

for i in range(n-1):
    sfd[i] = list(map(int,input().split()))


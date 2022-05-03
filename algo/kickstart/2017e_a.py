# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 10:08:41 2019

@author: kjh1
"""

T = int(input())

s = input()

dp = [[0]*100 for i in range(100)]

for i in range(len(s)):
    for j in range(len(s)):
        if_
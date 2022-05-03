# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 16:01:37 2020

@author: kjh1
"""

r,c = map(int,input().split())

left_to_right = [[0]*c for _ in range(r)]
right_to_left = [[0]*c for _ in range(r)]
up_to_down = [[0]*r for _ in range(2)]
down_to_up = [[0]*r for _ in range(2)]

for i in range(r):
    line = list(map(int,input().split()))
    for j in range(1,c):
        left_to_right[i][j] = left_to_right[i][j-1] + line[j-1]
        right_to_left[i][c-j-1] = right_to_left[i][c-j] + line[c-j]
        
    if(i < r-1):
        up_to_down[0][i+1] = up_to_down[0][i] + line[0]
        up_to_down[1][i+1] = up_to_down[1][i] + line[-1]
        
        down_to_up[0][r-i-2] = down_to_up[0][r-i-1] + left_to_right[r-i-1][1]
        down_to_up[1][r-i-2] = down_to_up[1][r-i-1] + left_to_right[r-i-1][-2]
        
print(left_to_right)
print(right_to_left)
print(up_to_down)
print(down_to_up)
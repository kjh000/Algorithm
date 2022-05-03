# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 14:42:40 2019

@author: kjh1
"""
import queue

T = int(input())

def isInside(a,b):
        return((a>= 0 and a<r) and (b>= 0 and b<c))
    
    
for t in range(T):
    
    q1 = queue.Queue()
    q2 = queue.Queue()
    
    r,c = map(int,input().split())
    visit1 = []
    visit2 = []
    direc = [[1,0],[-1,0],[0,1],[0,-1]]
    
    big = [0,[0,0]]
    
    
    mat = [[0]*c for _ in range(r)]
    
    
    
    for i in range(r):
        line = input()
        
        for j in range(c):
            if(line[j] == '1'):
                visit1.append([i,j])
                visit2.append([i,j])
                q1.put_nowait([i,j])
                q2.put_nowait([i,j])
    
    
    while not q1.empty():
        
        current = q1.get_nowait()
        cur_y = current[0]
        cur_x = current[1]
        
        for i in range(4):
            next_y = cur_y + direc[i][0]
            next_x = cur_x + direc[i][1]
            
            if(isInside(next_y,next_x) and [next_y,next_x] not in visit1):
                mat[next_y][next_x] = mat[cur_y][cur_x] + 1
                q1.put_nowait([next_y,next_x])
                visit1.append([next_y,next_x])
                if(mat[next_y][next_x]>big[0]):
                    big = [mat[next_y][next_x],[next_y,next_x]]
#                
#    if(big[0] > 0):
#        
#        mat = [[0]*c for _ in range(r)]
#        
#    
#        visit2.append(big[1])
#        q2.put_nowait(big[1])
#        
#        big = [0,[0,0]]
#    
#        
#        while not q2.empty():
#            
#            current = q2.get_nowait()
#            cur_y = current[0]
#            cur_x = current[1]
#            
#            for i in range(4):
#                next_y = cur_y + direc[i][0]
#                next_x = cur_x + direc[i][1]
#                
#                if(isInside(next_y,next_x) and [next_y,next_x] not in visit2):
#                    mat[next_y][next_x] = mat[cur_y][cur_x] + 1
#                    q2.put_nowait([next_y,next_x])
#                    visit2.append([next_y,next_x])
#                    if(mat[next_y][next_x]>big[0]):
#                        big = [mat[next_y][next_x],[next_y,next_x]]
#                  
                    
    print('Case #{}: {}'.format(t+1,big[0]))
    print(mat)
                
                
                
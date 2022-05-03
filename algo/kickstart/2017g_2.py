# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 12:21:29 2019

@author: kjh1
"""
import numpy as np

class Prim:
    def __init__(self):
        self.matrix = makeGraph()
        self.matrixLen = len(self.matrix[0])
        self.connected_Weight = np.zeros((self.matrixLen, self.matrixLen))
        self.visited_Vertex = np.zeros(self.matrixLen)
        self.connected_len = 0
        self.totalWeight = 0

    def cycleCheck(self, input_i, input_j):
        chk = False
        arr = []
        visited = np.zeros(self.matrixLen)
        arr.append(input_i)
        visited[input_i] = 1
        while (len(arr)):
            temp = arr.pop()
            if (chk == True):
                return chk
            for i in range(len(self.matrix[0])):
                if ( (self.connected_Weight[temp][i] == 1 or self.connected_Weight[temp][i] == 2) and visited[i] != 1 and temp != i ):
                    if (input_j == i):
                        chk = True
                        return chk
                    else:
                        arr.append(i)
                        visited[i] = 1
                    temp = i
        return chk

    def findLowerValue(self):
        lowest =(10**9)+1
        low_i ,low_j =0, 0
        for i in range(len(self.matrix[0])):
            if ( self.visited_Vertex[i] == 1):
                for j in range(len(self.matrix[0])):
                    if( i != j):
                        chk = self.cycleCheck(i, j)
                        if( chk):
                            self.connected_Weight[i][j] = 2
                            self.connected_Weight[j][i] = 2
                        elif(chk == False and self.matrix[i][j] != 0 and  self.connected_Weight[i][j] != 1  and self.connected_Weight[i][j] != 2):
                            if(self.matrix[i][j] <= lowest):
                                lowest,low_i, low_j = self.matrix[i][j], i,j

        return int(lowest),low_i,low_j

    def Prim(self):
        index = 0
        self.visited_Vertex[index] = 1
        while (self.connected_len < self.matrixLen-1):
            lowest, i, j = self.findLowerValue()
            self.visited_Vertex[i] = 1
            self.visited_Vertex[j] = 1
            self.connected_Weight[i][j] = 1
            self.connected_Weight[j][i] = 1
            self.connected_len += 1
            self.totalWeight += lowest
#            print(self.totalWeight)
        return self.totalWeight


T = int(input())

for t in range(T):
    N = int(input())
    r = list(map(int,input().split()))
    b = list(map(int,input().split()))
    INF = (10**9)+1
    rb = []
    
    for i in range(N):
        rb.append((r[i],b[i]))
    
    total = 0
    
    mini = []
    
    def makeGraph():
        xor = [[] for i in range(N)]
        for i in range(N):
            for j in range(N):
                if(i == j):
                    xor[i].append(INF)
                else:
                    xor[i].append(min((rb[i][0]^rb[j][1],rb[i][1]^rb[j][0])))
        return xor
    
    
    Prim().Prim()
#    print(Prim().Prim())
    print('Case #{}: {}'.format(t+1,Prim().Prim()))
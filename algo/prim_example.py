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
        lowest =100
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
        total = 0
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
#            print("(", i, ",", j, ")-> weight: ", lowest, "total Weight :", self.totalWeight)
            total = self.totalWeight
            
        return total
            

def makeGraph():
    matrix = [[2]*3 for i in range(3)]

#    for i in range(3):
#        matrix[i] = list(map(int,input().split()))
#    return matrix

    a,b = map(int,input().split())

    matrix[a-1][b-1] = 1
    matrix[b-1][a-1] = 1

    return matrix

print(Prim().Prim())






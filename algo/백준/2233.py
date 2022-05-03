# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:04:37 2019

@author: kjh1
"""

n = int(input())

arr = input()

x,y = map(int,input().split())

mat = []
stack = []
tree = [[] for i in range(n)]
parents = [[] for i in range(n)]

x_parents = []
y_parents = []
node = 0
cut = 0

ii = -1
jj = -1

mat.append(node)
stack.append(node)
node += 1


for i in range(1,2*n):
    if(arr[i] == '0'):
        
        mat.append(node)
        tree[stack[-1]].append(node)
        stack.append(node)
        node += 1
        
    elif(arr[i] == '1'):
        
        a = stack.pop()
        mat.append(a)
        

xx = mat[x-1]
yy = mat[y-1]

for i in range(n):
    if(tree[i]):
        for j in range(len(tree[i])):

            parents[tree[i][j]] = i
            
    else:
        pass
    
def find_parents(arr,node):
    if(parents[node] == 0 or node == 0):
        arr.append(0)
        return
    else:
        arr.append(parents[node])
        find_parents(arr,parents[node])

find_parents(x_parents,xx)
find_parents(y_parents,yy)
x_parents.append(xx)
y_parents.append(yy)

cut = max(set(x_parents) & set(y_parents))

for i in range(2*n):
    if(mat[i] == cut and ii == -1):
        ii = i+1
    
    elif(mat[i] == cut and jj == -1):
        jj = i+1
        

print(ii,jj)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
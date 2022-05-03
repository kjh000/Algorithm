# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 16:43:17 2019

@author: kjh1
"""

n = int(input())
m = int(input())

q = []
result = []

cities = [[] for i in range(n+1)]
indegree = [0]*(n+1)


for i in range(m):
    
    a,b = map(int,input().split())
    indegree[a] += 1
    
    cities[a].append(b)
    
    

for i in range(1,n+1):
    
    if(indegree[i] == 0):
        q.append(i)
   
    
while q:
    
     cur = q.pop()
     result.append(cur)
     
     for i in cities[cur]:
         
         indegree[i] -= 1
         if(indegree[i] == 0):
             q.append(i)


print(result)
    
    
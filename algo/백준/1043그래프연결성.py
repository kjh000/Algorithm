# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 15:18:05 2019

@author: kjh1
"""

n,m = map(int,input().split())
know = list(map(int,input().split()))
wise = know[1:]
#party = [list(map(int,input().split())) for _ in range(m)]

party = {}
people = {}

visited_party = [-1]*(m+1)
check = [-1]*(n+1)

for i in range(n):
    people[i+1] = []


for i in range(m):
    
    party[i+1] = []
    l = list(map(int,input().split()))

    for j in range(l[0]):
        party[i+1].append(l[j+1])
        people[l[j+1]].append(i+1)
        
q = []

for i in range(know[0]):
    q.append(wise[i])
    
while q:
    
    cur = q.pop()
    
    for i in range(len(people[cur])):
        
        if(visited_party[people[cur][i]] == -1):
           visited_party[people[cur][i]] = 1
           
           for j in range(len(party[people[cur][i]])):
               if(check[party[people[cur][i]][j]] == -1):
                  check[party[people[cur][i]][j]] = 1
                  
                  q.append(party[people[cur][i]][j])

print(m - visited_party.count(1))
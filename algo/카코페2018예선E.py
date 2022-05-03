# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 17:08:11 2019

@author: kjh1
"""
import sys

n,q,j = map(int,input().split())

total = [0]*(n+1) ## 누적합
score = [0]*(q+1) ## 루트에서 전파할 점수
root = [0]*(q+1) ## i번째 쿼리 시 시작 노드

lo = [0]*(n+1) ## i번째 가수가 몇번째 쿼리부터 목표점수를 넘길수있는지 하한 
hi = [0]*(n+1) ## "" 상한

predicted_to = {} ## i번째 가수가 q번째 쿼리를 돌리고 나서야 목표점수 달성

T = [[0,0]] ## i query at T time
## get : point query
def get(idxg):
    sumation1 = 0
    while(idxg>0):
        sumation1 += total[idxg]
        idxg -= idxg&(-idxg)

    return sumation1

## lazy propagation for point query 
def update(idx,val):
    while(idx<=n):
        total[idx] += val
        idx += idx&(-idx)


def range_update(q):
    node = root[q]
    length = affects[node][1] - affects[node][0] + 1
    updated_score = score[q]//length

    update(affects[node][0],updated_score)
    update(affects[node][1],-updated_score)    
    
mat = list(map(int,input().split()))
#mat = list(map(int,sys.stdin.readline().split()))
songs = list(map(int,input().split()))
#songs = list(map(int,sys.stdin.readline().split()))
songs.insert(0,0)
tps = []

tree = {}
ordering = {}
visited = {}
affects = {}
singers = {}

idxa = 1
def dfs(u):
    global idx
    l = idx
    visited[u] = True
    ordering[u] = idx
    
    for i in tree[u]:
        if(visited[i] == False):
            idx += 1
            dfs(i)
    r = idx
    affects[u] = [l,r]
    

for i in range(1,n+1):
    tree[i] = []
    ordering[i] = 0
    visited[i] = False
    affects[i] = None
    singers[i] = []
#    predicted_to[i] = []
    
for i in range(n-1):
    tree[mat[i]].append(i+2)
#    tree[i+2].append(mat[i])
    
for i in range(1,n+1):
    singers[songs[i]].append(i)
    
dfs(1)

for i in range(1,q+1):
    t,p,s = map(int,input().split())
#    t,p,s = map(int,sys.stdin.readline().split())
    T.append([t,i])
    root[i] = p
    score[i] = s
    predicted_to[i] = []

T.sort()

for i in range(1,n+1):
    
    hi[i] = q+1
    if(len(singers[i]) == 0):
        lo[i] = q+1
    else:
        lo[i] = 1
        
    
change= True

while change:
    
    total = [0]*(n+1)
    
    for i in range(1,n+1):
        if(lo[i] != hi[i]):

            predicted_to[(lo[i] + hi[i])//2].append(i)
            
        change = False
   
    for k in range(1,q+1):
        idx = T[k][1]
#        print(idx)
        range_update(idx)
        print(idx,get(1),get(2),get(3))
#        sumation = 0
        while(len(predicted_to[k]) > 0):
            
#            print(k,predicted_to[k])
            
            change = True
            singer_id = predicted_to[k].pop()
            
#            print(singer_id,predicted_to[k])
            sumation = 0
            goal_score = j*(len(singers[singer_id]))
          
            for song in singers[singer_id]:
                sumation += get(ordering[song])
                if(sumation >= goal_score): 
#                    print('wow!')
                    break
            
            if(sumation > goal_score): hi[singer_id] = k
            else: lo[singer_id] = k+1

            
for i in range(1,n+1):
    if(lo[songs[i]] <= q):
        print(T[lo[songs[i]]][0])
    else:
        print(-1)

print(ordering)
#print(lo)
#print(hi)
#print(singers)
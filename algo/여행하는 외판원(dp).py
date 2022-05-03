import sys
import math

INF = math.inf

n = int(input())

#dist = [[0]*(n+1) for _ in range(n+1)]
dist = []
memo = [[-1]*(1<<(n+1)) for _ in range(n+1)]

def shortestPath(here,visited):
    if visited == (1<<n) -1 :
        return dist[here][0]
    
    if memo[here][visited] >= 0:
        return memo[here][visited]
    
    memo[here][visited] = INF
    for next in range(n):
        if visited & (1<<next):
            continue
        cand = dist[here][next] + shortestPath(next,visited+(1<<next))
        
        memo[here][visited] = min(memo[here][visited],cand)
        
    return memo[here][visited]
    

for i in range(n):
    dist.append(list(map(int,input().split())))
    
    
ans = shortestPath(0,1)
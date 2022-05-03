# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:10:45 2019

@author: kjh1
"""

import sys
import heapq

INF = sys.maxsize

def solve(adjacent, K):
    prev = [-1] * (len(adjacent) + 1)    
    dist = [INF] * (len(adjacent) + 1)   
    dist[K] = 0

    priority_queue = []
    heapq.heappush(priority_queue, [0, K])

    while priority_queue:
        
        current_dist, here = heapq.heappop(priority_queue)

        
        for there, length in adjacent[here].items():
            next_dist = dist[here] + length

            if next_dist < dist[there]:
                dist[there] = next_dist
                prev[there] = here
                heapq.heappush(priority_queue, [next_dist, there])

    return dist, prev

V, E = map(int, input().split())
K = int(input())
adjacent = [{} for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())

    if v in adjacent[u]:
        adjacent[u][v] = min(adjacent[u][v], w)
    else:
        adjacent[u][v] = w

dist, prev = solve(adjacent, K)

for d in dist[1:]:
    print(d if d != INF else "INF")
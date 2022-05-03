# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 23:58:54 2019

@author: kjh1
"""

graph = [[1]*3 for _ in range(3)]

edges = 3
vertices = 3
T = set();
X = set();

# select an arbitrary vertex to begin with
X.add(0);

while len(X) != vertices:
    crossing = set();
    # for each element x in X, add the edge (x, k) to crossing if
    # k is not in X
    for x in X:
        for k in range(vertices):
            if k not in X and graph[x][k] != 0:
                crossing.add((x, k,graph[x][k]))
    # find the edge with the smallest weight in crossing
    edge = sorted(crossing, key=lambda e:graph[e[0]][e[1]])[0];
    # add this edge to T
    T.add(edge)
    # add the new vertex to X
    X.add(edge[1])

# print the edges of the MST
#for edge in T:
#    print (edge)
#    
print(T)
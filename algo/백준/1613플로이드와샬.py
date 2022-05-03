
import sys

INF = sys.maxsize

n,m = map(int,input().split())

mat = [[INF]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if(i == j):
            mat[i][j] = 0

for i in range(m):
    a,b = map(int,input().split())
    mat[a-1][b-1] = 1
    

for k in range(n):
    for i in range(n):
        for j in range(n):
            if(mat[i][k] != INF and mat[k][j] != INF):
                mat[i][j] = min(mat[i][k] + mat[k][j], mat[i][j])
                

s = int(input())

for i in range(s):
    a,b = map(int,input().split())
    
    if(mat[a-1][b-1] == INF and mat[b-1][a-1] == INF):
        print(0)
    
    elif(mat[a-1][b-1] != INF and mat[b-1][a-1] == INF):
        print(-1)
        
    else:
        print(1)
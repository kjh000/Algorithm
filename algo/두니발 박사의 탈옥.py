"""
search(here,d) : percentage of finding at here after d days
"""


n,d,p = map(int,input().split())
connected = []
memo = [[-1]*(d+1) for _ in range(n+1)]

for i in range(n):
    connected.append(list(map(int,input().split())))
t = int(input())
q = list(map(int,input().split()))

deg = [0]*(n+1)

for i in range(n):
    for j in range(n):
        if connected[i][j] == 1:
            deg[j] += 1

def search(here,days):
    if days == 0:
        if here == p:
            return 1.0
        else:
            return 0.0
    if memo[here][days] > -0.5:
        return memo[here][days]
    
    memo[here][days] = 0.0
    
    for there in range(n):
        if connected[here][there] == 1:
            memo[here][days] += search(there,days - 1)/deg[there]
        
    return memo[here][days]


for i in q:
    print(search(i,d))
import sys
import math
import heapq

INF = math.inf

n,r = map(int,input().split())
c = [0]
cc = list(map(int,input().split()))
c.extend(cc)

nc = c[:]
cnt = [1]*(n+1)
parent = [0]*(n+1)
children = {}
group = {}
visit = [0]*(n+1)
visit[r] = 1
ans = 0
now = 1

for i in range(n):
    children[i+1] = []
    group[i+1] = [i+1]
    
for i in range(n-1):
    u,v = map(int,input().split())
    parent[v] = u
    children[u].append(v)
    
def findMax():
    idx = -1
    maxi = -INF
    
    for i,num in enumerate(nc):
        if  i!= 0 and i != r and visit[i] == 0 and maxi < nc[i]/cnt[i]:
            maxi = nc[i]/cnt[i]
            idx = i
    
    visit[idx] = 1
    return idx


while True:
    cur = findMax()
    if cur == -1 : break
    
    pc = parent[cur]
    
    if pc == r:
        group[pc].extend(group[cur])
        for node in group[cur]:
            for nn in children[node]:
                parent[nn] = pc
        
        continue
    else:
        group[pc].extend(group[cur])
        nc[pc] += nc[cur]
        cnt[pc] += cnt[cur]
        for node in group[cur]:
            for nn in children[node]:
                parent[nn] = pc
print(group)

for idx,num in enumerate(group[r]):
    ans += (idx+1)*c[num]
    
print(ans)
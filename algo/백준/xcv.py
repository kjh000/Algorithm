import sys
import math
import heapq
INF = math.inf

n,r = map(int,input().split())
c = [0]
cc = list(map(int,input().split()))
c.extend(cc)

mean = c[:]
total = c[:]
parent = {}
children = {}
childMean = {}
stick = [0]*(n+1)
stick[r] = 1
ans = c[r]
now = 2
group = {}
visit = [0]*(n+1)
visit[r] = 1
vitsum = 1
cnt = [1]*(n+1)
heap = []

for i in range(n):
    children[i+1] = []
    childMean[i+1] = []
    group[i+1] = [i+1]
    
for i in range(n-1):
    u,v = map(int,input().split())
    parent[v] = u
    children[u].append(v)
    
    
def find_max():
    idx = 0
    maxi = -INF
    
    for i,num in enumerate(mean):
        if i != 0 and i != r and num > maxi and visit[i] == 0:
            maxi = num
            idx = i
    visit[idx] = 1 
    return idx


while True:
    
    k = find_max()
#    print(k)
    if k == 0: break
    pk = parent[k]
    if pk == r: continue
    while True:
        if mean[pk] <(total[pk] + total[k])/(cnt[pk] + cnt[k]) :
#        print(k,cnt[pk],cnt[k])
            cnt[pk] += cnt[k]
            total[pk] += total[k]
            mean[pk] = total[pk]/cnt[pk]
            visit[pk] = 1
            k = pk
            pk = parent[pk]
            
        else:
            
            pk = parent[pk]
            
        if pk == r: break


print(mean)
for node in children[r]:
    heapq.heappush(heap,[-mean[node],-c[node],node])
    
while heap:

    cur = heapq.heappop(heap)
    
    ans += now*(c[cur[2]])
    now += 1
    
    if children[cur[2]]:
        for i in children[cur[2]]:
            heapq.heappush(heap,[-mean[i],-c[i],i])
            
print(ans)

print(total)
print(cnt)

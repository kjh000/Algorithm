import sys

v = int(input())
#e = int(input())
e = v-1
visit = [0]*(v+1)
adj = {}
choose = [0]

for i in range(v):
    adj[i+1] = []
    
for i in range(e):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
    
def dfs(here):

    visit[here] = 1
    children = [0,0,0]
    for i in adj[here]:
        there = i
        if visit[there] == 0:

            children[dfs(there)] += 1
            
    if children[0] != 0:
        choose[0] += 1
        return 2
    
    if children[2] != 0:
        return 1
    return 0

#dfs(1)

for j in range(1,v+1):
    

    if visit[j] == 0 :
        if dfs(j) == 0:
#            print(j)
            choose[0] += 1

print(choose[0])
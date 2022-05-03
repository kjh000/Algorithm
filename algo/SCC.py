'''
assume all SCC are connected
if not -> dfs all nodes
v : # of nodes, e : # of edges
a,b : a -> b
O(v + e)
'''

v,e = map(int,input().split())

mat = {}
rev_mat = {}
stack = []
scc = {}
for i in range(v):
    mat[i+1] = []
    rev_mat[i+1] = []
    scc[i+1] = []
    
    
for i in range(e):
    a,b = map(int,input().split())
    mat[a].append(b)
    rev_mat[b].append(a)
    
visit = [0]*(v+1)

def DFS(start):
    visit[start] = 1
    
    for node in mat[start]:
        if visit[node] == 0:
            DFS(node)
    stack.append(start)
    
DFS(1)

visit = [0]*(v+1)
cc
def findSCC(node,start):
    visit[node] = 1
    scc[start].append(node)
    for next in rev_mat[node]:
        if visit[next] == 0:
            findSCC(next,start)
            
while stack:
    now = stack.pop()
    if visit[now] == 1:
        continue
    findSCC(now,now)
    
print(scc)
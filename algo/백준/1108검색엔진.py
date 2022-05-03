import sys

n = int(input())
mat = {}
rev_mat = {}
scc = {}

stack = []
numbering = {}
web = []
q = []
point = {}
head = {}
zip = {}

for i in range(n):
    line = list(input().split())
    q.append(line)
    for j in range(len(line)):
        if j == 1: continue
        web.append(line[j])

web = list(set(web))
web.sort()

lw = len(web)

visit = [0]*(lw + 1)
new_visit =  [0]*(lw + 1)

for i in range(lw):
    numbering[web[i]] = i+1
    
for i in numbering:
    mat[numbering[i]] = []
    rev_mat[numbering[i]] = []
    scc[numbering[i]] = []
    head[numbering[i]] = numbering[i]
    point[numbering[i]] = 1
    
    
for i in range(n):
    line = q[i]
    end = numbering[line[0]]
    e = int(line[1])
    for j in range(e):
        start = numbering[line[j+2]]
        mat[start].append(end)
        rev_mat[end].append(start)


def DFS(start):
    visit[start] = 1
    
    for node in mat[start]:
        if visit[node] == 0:
            DFS(node)
    stack.append(start)

for node in range(1,lw+1):
    if visit[node] == 1: continue
    DFS(node)
    
visit = [0]*(lw + 1)


def findSCC(node,start):
    visit[node] = 1
    scc[start].append(node)
    head[node] = start
    zip[start] = []
    for next in rev_mat[node]:
        if visit[next] == 0:
            findSCC(next,start)
            

while stack:
    now = stack.pop()
    if visit[now] == 1:
        continue
    findSCC(now,now)
    
for i in mat:
    for j in mat[i]:
        zip[head[i]].append(head[j])
        
def scoring(start):
    for next in zip[start]:
        point[next] += 1
        scoring(next)
        
for i in zip:
    if zip[i]:
        scoring(i)
            
qq = input()
nq = numbering[qq]
print(point[head[nq]])

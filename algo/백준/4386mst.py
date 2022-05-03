
parent = {}
rank = {}

def distance(p1,p2):
    l = (p1[0] - p2[0])**2 + (p1[1]-p2[1])**2
    return l**(0.5)


def make_set(v):
    parent[v] = v
    rank[v] = 0
    
def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
        
    return parent[v]



def union(v,u):
    
    root1 = find(v)
    root2 = find(u)

    
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            
            if rank[root1] == rank[root2]:
                rank[root2] += 1
                
                
def kruskal(graph):
    for v in graph['vertices']:
        make_set(v)
        
    mst = []
    
    edges = graph['edges']
    edges.sort()
    
    for edge in edges:
        weight,v, u = edge
        
        if find(v) != find(u):
            union(v,u)
            mst.append(edge)
            
    return mst


graph = {
        'vertices' : [],
        'edges' : []       
        }


n = int(input())
points = []

for i in range(n):
    graph['vertices'].append(i+1)
    x,y = map(float,input().split())
    points.append([x,y])
    
for i in range(n):
    for j in range(n):
        if i == j:
            pass
        graph['edges'].append([distance(points[i],points[j]),i+1,j+1])
        
mst = kruskal(graph)

    
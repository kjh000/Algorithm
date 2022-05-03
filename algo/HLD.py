"""
chain : start from ith node -> store in chain[i], parent -> child
depth : # of other chain to reach route node
chainNumber : each node belongs to 
chainIndex : ith  in its chain , start from 0
"""
n = 7
Edge = {1 : [2,3], 2: [4,5], 3:[6,7],4:[],5:[],6:[],7:[]}

parent = [0]*(n+1)
volume = [0]*(n+1)

chain = [[] for _ in range(n+1)]
chainNumber = [0]*(n+1)
chainIndex= [0]*(n+1)
depth = [0]*(n+1)


visit = [0]*(n+1)

def dfs(here,p):
    
    parent[here] = p
    volume[here] = 1
        
    
    for there in Edge[here]:
        
        if there != p:
            volume[here] += dfs(there,here)
    
    return volume[here]



def HLD(i,p,cur_chain,d):
    depth[i] = d
    chainNumber[i] = cur_chain
    chainIndex[i] = len(chain[cur_chain])
    chain[cur_chain].append(i)
    
    heavy = -1
    
    for x in Edge[i]:
        if x != p and (heavy == -1 or volume[x] > volume[heavy]):
            heavy = x
            
    if heavy != -1:
        HLD(heavy,i,cur_chain,d)
    
    for x in Edge[i]:
        if x != p and x != heavy:
            HLD(x,i,x,d+1)
            
def LCA(a,b):
    while chainNumber[a] != chainNumber[b]:
        if depth[a] > depth[b]:
            a = parent[chainNumber[a]]
            
        else:
            b = parent[chainNumber[b]]
            
    if chainIndex[a] > chainIndex[b]: return b
    else:
        return a
            
dfs(1,0)
HLD(1,0,1,0)

print(chain)
print(chainIndex)
print(chainNumber)
print(depth)


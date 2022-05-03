import sys

INF = sys.maxsize
MAX_V = 2020
S = MAX_V - 2
T = MAX_V - 1

class Edge(object):
    
    def __init__(self,v,co,ca,fl,re):
        self.v = v
        self.cost = co
        self.cap = ca
        self.flow = fl
        self.rev = re
        
adj = [[] for _ in range(MAX_V)]

def add_Edge(here,nextt,cost,cap):
    adj[here].append(Edge(nextt,cost,cap,0,len(adj[nextt])))
    adj[nextt].append(Edge(here,-cost,0,0,len(adj[here])-1))
    
def MCMF(adj):
    result = 0
    while 1:
        
        q = []    
        vPrev = [-1]*(MAX_V)
        ePrev = [-1]*(MAX_V)
        dist = [INF]*(MAX_V)
        inQ  = [False]*(MAX_V)
        
        dist[S] = 0
        inQ[S] = True    
        
        q.append(S)
        
        while q:
            here = q.pop()
            inQ[here] = False
            
            for i in range(len(adj[here])):
                nextt = adj[here][i].v
                c = adj[here][i].cap
                f = adj[here][i].flow
                d = adj[here][i].cost
                
                if(c - f> 0 and dist[nextt] > dist[here] + d):
                    dist[nextt] = dist[here] + d
                    vPrev[nextt] = here
                    ePrev[nextt] = i
                    
                    if (inQ[nextt] == False):
                        q.append(nextt)
                        inQ[nextt] = True
                        
                        
        if q:
            if(dist[q[-1]]<dist[q[0]]):
                u = q.pop()
                q.insert(0,u)
                       
        if(vPrev[T] == -1):
            break
        
        
        flow = INF
        
        cur = T
        
        while cur != S:
    
            prev =vPrev[cur]
            idx = ePrev[cur]
            flow = min(flow,adj[prev][idx].cap - adj[prev][idx].flow)
            cur = vPrev[cur]
            
        cur = T
        
        while cur != S:
            prev = vPrev[cur]
            idx = ePrev[cur]
            
            result += adj[prev][idx].cost*flow
            
            adj[prev][idx].flow += flow
            adj[cur][adj[prev][idx].rev].flow -= flow
            
            cur = vPrev[cur]
            
    return result
    
while 1:
    
    try:
        adj = [[] for _ in range(MAX_V)]
        
        n,m = map(int,input().split())
#        n,m = map(int,sys.stdin.realine().split())
        
        if(n == ''): break
        
        for i in range(1,n+1):
            if(i == 1 or i == n):
                add_Edge(i,i+n,0,2)
            else:
                add_Edge(i,i+n,0,1)
        
        for i in range(m):
            
            a,b,c = map(int,input().split())
            add_Edge(a+n,b,c,1)
            
        add_Edge(S,1,0,2)
        add_Edge(n,T,0,2)
        
    
        ans = MCMF(adj)    
                
        print(ans)
    except :
        break
            
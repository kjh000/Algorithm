import sys
n,m = map(int,input().split())
INF = sys.maxsize

graph = []
for i in range(m):
    u,v,w = map(int,input().split())
    graph.append([u,v,-w])


bf = [INF] * (n+1)
def solve_bf():
    line = [0]*(n+1)
    back = [n]
    bf[1] = 0
    minus = False
    for i in range(n):
        for j in range(m):
            v = graph[j][0]
            nv = graph[j][1]
            w = graph[j][2]
            if bf[v] != INF and bf[nv] > bf[v] + w:
                line[nv] = v
                bf[nv] = bf[v] + w
                if i == n-1:
                    minus = True
    if minus:
        print(-1)
    else:
        
        if(bf[n] == INF):
            print(-1)
        else:
            cur = line[n]
            cnt = 0
            while 1:
                
                if(cur == 1):
                    break
                
                if(cnt > n):
                    break
                back.append(cur)
                cur = line[cur]
                
                    
    back.reverse()
    
    print(1,end = ' ')
    for i in back:
        print(i,end= ' ')            
            
            
            
solve_bf()
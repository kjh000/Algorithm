
import sys
INF = sys.maxsize

#
V,E = map(int,input().split())

a,b,k,g = map(int,input().split())
g_visit = list(map(int,input().split()))



def dijkstra(a,V,graph):
#    
#    INF = sys.maxsize
    
    s =[False]*V
#    time = [k]*V
    d = [INF]*V 

    d[a-1] = 0
    
    
    while True:
        
        m = INF
        N = -1
        
        for j in range(V):
            if not s[j] and m >d[j]:
                m = d[j]
                N = j
                
                
        if m == INF:
            break
        
        s[N] = True
        
        
        for j in range(V):
            
            if s[j]: continue
            via = d[N] + graph[N][j]
            
            if d[j]>via:
#                d[j] = via
#                print(g_time[N][j])
                if(g_time[N][j] != INF):
#                    print(via,g_time[N][j])
                    if(d[N] + k < g_time[N][j][0] or d[N] + k >= g_time[N][j][1]):
                        d[j] = via
                    else:
                        d[j] = via + g_time[N][j][1] - (d[N]+k)
    #                    time[j] = k + via
                else:
#                    print(via,'INF')
                    d[j] = via
                
    return d

#V,E = map(int,input().split())
#K = int(input())
#INF = sys.maxsize
graph = [[INF]*V for _ in range(V)]
g_time = [[INF]*V for _ in range(V)]

for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u-1][v-1] = w
    graph[v-1][u-1] = w
    
tmp = 0
for i in range(g-1):
    aa,bb = g_visit[i],g_visit[i+1]
    g_time[aa-1][bb-1] = [tmp,graph[aa-1][bb-1] + tmp]
    g_time[bb-1][aa-1] = [tmp,graph[bb-1][aa-1] + tmp]
    
    tmp = g_time[aa-1][bb-1][1]


ans = dijkstra(a,V,graph)

print(ans[b-1])


#for d in dijkstra(a,V,graph):
#    print(d if d!= INF else 'INF')
#    
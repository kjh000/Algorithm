import sys
import queue
import heapq

dx = [0,0,1,-1]
dy = [1,-1,0,0]

n,m = map(int,input().split())
mat = []
mini = 10**9

visit = [[0]*m for _ in range(n)]

dist = [[0]*m for _ in range(n)]
q = queue.Queue()
start = []
end = []
h = []

def is_Inside(x,y):
    if x <0 or y<0 or x>=m or y>=n:
        return False
    return True
    
for i in range(n):
    line = input()
    mat.append(line)
    for j in range(m):
        if line[j] == '+':
            visit[i][j] = 1
            q.put([i,j])
        if line[j] == 'V':
            start = [i,j]
        if line[j] == 'J':
            end = [i,j]
        
while not q.empty():
    now = q.get()
    y = now[0]
    x = now[1]
    visit[y][x] = 1
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if is_Inside(nx,ny) :
            if visit[ny][nx] != 1:
                dist[ny][nx] = dist[y][x] + 1
                visit[ny][nx] = 1
                q.put([ny,nx])
                
                
sy,sx = start[0],start[1]

heapq.heappush(h,[-dist[sy][sx],dist[sy][sx],[sy,sx]])


while h:
    
    now = heapq.heappop(h)
    d = now[1]
    mini = min(mini,d)
    
    node = now[2]
    y = node[0]
    x = node[1]
    
    if dist[y][x] == -1:
        continue
    dist[y][x] = -1
#    visit[y][x] = 1
    if mat[y][x] == 'J':
        break
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if is_Inside(nx,ny):
            if dist[ny][nx] != -1:
                dist[ny][nx] = -1
                heapq.heappush(h,[-dist[ny][nx],dist[ny][nx],[ny,nx]])
                
print(mini)
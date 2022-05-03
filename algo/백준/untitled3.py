import sys

dx = [1,-1,0,0]
dy = [0,0,1,-1]
visit = [0]*26
ans = [0]

R,C = map(int,input().split())

mat = [list(input()) for _ in range(R)]


def isPossible(x,y,check):
    if check[mat[y][x]] == 0:
        return True
    else:
        return False
def go(y,x,cnt):
    
    ans[0] = max(ans[0],cnt)
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if ny<0 or ny>=R or nx<0 or nx>=C:
            continue
        k = ord(mat[ny][nx]) - 65
        if visit[k] != 0:
            continue
        
        visit[k] += 1
        go(ny,nx,cnt+1)
        visit[k] -= 1
        
visit[ord(mat[0][0])-65] = 1

go(0,0,1)
print(ans[0])
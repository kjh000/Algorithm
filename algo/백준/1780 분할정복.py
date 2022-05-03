
MAX_N = 2188

N = int(input())

#paper = [[0]*MAX_N for _ in range(MAX_N)]
paper = [list(map(int,input().split())) for _ in range(N)]


cnt = [0]*3

def same(x,y,n):
    for i in range(x,x+n):
        for j in range(y,y+n):
            if paper[x][y] != paper[i][j]:
                return False
            
    return True

def solve(x,y,n):
    if same(x,y,n):
        cnt[paper[x][y] + 1] += 1
        return
    
    m = n//3
    
    for i in range(3):
        for j in range(3):
            solve(x+i*m,y+j*m,m)
            
             
solve(0,0,N)

print(cnt)
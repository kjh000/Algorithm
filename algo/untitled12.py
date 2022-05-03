import sys

T = int(input())

for t in range(T):
    
    n,k = map(int,input().split())
    
    mat = list(map(int,input().split()))
    
    point = k
    
    ans = 0
    
    for i in range(n):
        if mat[i] == point:
            point -= 1
            
            if mat[i] == 1:
                ans += 1
                point = k
        else:
            if mat[i] == k:
                point = k-1
            else:
                
                point = k
            
    print('Case #{}: {}'.format(t+1,ans))
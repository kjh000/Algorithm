import sys

T = int(input())

for t in range(T):
    
    n = int(input())
    H = list(map(int,input().split()))
    print(H)
    
    peak = 0
    for i in range(n):
        if i == 0 or n-1:
            continue
        if H[i] > H[i-1]:
            peak += 1
            print('peak')
            
    print('Case #{}: {}'.format(t+1,peak))
import sys
import math

INF = math.inf

T = int(input())
for t in range(T):
    w,n = map(int,input().split())
    
    x = list(map(int,input().split()))
    x.sort()
    mini = INF
    for i in range(w):
        target = x[i]
        ans = 0
        for j in range(w):
            a = x[j]
            b = x[j] + n
            
            aa = abs(target - a)
            bb = abs(target - b)
            
            ans += min(aa,bb)
            
        mini = min(mini,ans)
        
        
    print('Case #{}: {}'.format(t+1,mini))
import sys

n = int(input())

t = [16]
p = [-1]
dp = [0]*(n+1)


for i in range(n):
    ti,pi = map(int,input().split())
    t.append(ti)
    p.append(pi)
    
if t[1] <= n:
    dp[1] = p[1]

for i in range(2,n+1):
    if n+1 - i < t[i]: continue
    for j in range(1,i):
        if i - j >= t[j]:
            dp[i] = max(dp[i],p[i] + dp[j])
        else:
            dp[i] = max(dp[i],p[i])
            
print(max(dp))
        
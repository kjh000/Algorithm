import sys

n = int(input())

wine = []
dp = [0]*(n)

for i in range(n):
    a = int(input())
    wine.append(a)

if n <= 2:
    print(sum(wine))
else:
    dp[0] = wine[0]
    dp[1] = dp[0] +wine[1]
    
    if wine[1] > wine[0]:
        dp[2] = wine[1] + wine[2]
    else:
        dp[2] = wine[0] + wine[2]
        
    dp[2] = max(dp[2],dp[1])
        
    for i in range(3,n):
        
        dp[i] = max(wine[i-1] + dp[i-3] + wine[i],dp[i-2] + wine[i])
        
        dp[i] = max(dp[i],dp[i-1])
        
    print(max(dp))

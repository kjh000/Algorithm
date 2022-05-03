
mod = 10**9

n = int(input())

dp = [[0]*11 for _ in range(n+1)]

dp[1] = [0,1,1,1,1,1,1,1,1,1,9]

for i in range(2,n+1):
    tot = 0
    for j in range(10):
        if j == 0:
            dp[i][0] = dp[i-1][1]
        elif j == 9:
            dp[i][9] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        
        tot += dp[i][j]
    
    dp[i][-1] = tot


print(dp[n][-1]%mod)    
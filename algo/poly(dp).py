
MOD = 10**7

memo = [[-1]*101 for _ in range(101)]
ret = [0]

def poly(n,first):
    if n == first: return 1
    
    if memo[n][first] != -1: return memo[n][first]
    memo[n][first] = 0
    
    for second in range(1,n-first+1):
        add = second + first - 1
        add *= poly(n-first,second)
        add %= MOD
        memo[n][first] += add
        memo[n][first] %= MOD
        
    return memo[n][first]

n = int(input())

neo_memo = [0]*(101)
ans = [0]*(101)

for i in range(1,n+1):
    neo_memo[i] = poly(i,1)
    

for i in range(1,n+1):
    if i == 1:
        ans[i] = neo_memo[i]
    else:
        ans[i] = (sum(ans[1:i]) + neo_memo[i])%MOD

print(ans[n])

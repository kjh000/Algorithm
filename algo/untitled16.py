import sys


BIG = 10**9 + 7
DNA = input()
n = int(input())

ld = len(DNA)

amino = ['A','C','G','T']
candi2 = {}
dp = []
candi3 = {}
arr = []

aminos = [0]*ld
ans = 0
dp3 = []

for i in range(4):
    for j in range(4):
        candi2[amino[i]+amino[j]] = 0
        for k in range(4):
            candi3[amino[i]+amino[j]+amino[k]] = 0

        
for i in range(ld):
    dic = candi2.copy()
    dp.append(dic)
    
    dic3 = candi3.copy()
    dp3.append(dic3)

for i in range(ld):

    for j in range(i+1,ld):
        
        dp[j][DNA[i]+DNA[j]] = dp[j-1][DNA[i]+DNA[j]] + 1
        
for i in range(1,ld):
    for c2 in dp[i]:
        dp[i][c2] += dp[i-1][c2]            

for i in range(2,ld):
    for c2 in candi2:
#        candi3[c2+DNA[i]] += dp[i-1][c2]
        dp3[i][c2+DNA[i]] += dp[i-1][c2]
        
for i in range(2,ld):
    tot = 0
    for c3 in candi3:
        tot += dp3[i][c3]
    aminos[i] = tot
    
print(aminos)

for i in range(n):
    cd ,ami = input().split()
    arr.append([cd,ami])
    
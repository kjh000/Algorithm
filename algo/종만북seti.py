
MOD = 2**32
N = 10**4
a = [0]*N
a[0] = 1983

for i in range(1,N):
    a[i] = (((a[i-1]*214013 + 2531011)%MOD)%10000)+1
    
print(a[:6])
    
import sys
import math
INF = math.inf
memo = [[-1]*11 for _ in range(101)]
ret = [0]

n,s = map(int,input().split())
mat = list(map(int,input().split()))
mat.sort()

psum = [0]*n
pSqsum = [0]*n
psum[0],pSqsum[0] = mat[0],mat[0]**2

for i in range(1,n):
    psum[i] = psum[i-1] + mat[i]
    pSqsum[i] = pSqsum[i-1] + mat[i]**2
    
def minError(lo,hi):
    if lo == 0:
        suma = psum[hi]
        sqsuma = pSqsum[hi]
    else:
        suma = psum[hi] - psum[lo-1]
        sqsuma = pSqsum[hi] - pSqsum[lo-1]
        
    m = int(0.5 + suma/(hi-lo + 1))
    
    ret1 = sqsuma - 2*m*suma + m*m*(hi-lo+1)
    return ret1

def quantize(fro,parts):
    if fro == n: return 0
    if parts == 0 : return INF
    
    ret[0] = memo[fro][parts]
    
    if ret[0] != -1: return ret[0]
    ret[0] = INF
    
    partSize = 1
    while True:
        ret[0] = min(ret[0],minError(fro,fro+partSize -1) + quantize(fro + partSize,parts-1))
        partSize += 1
        
        if fro + partSize > n: break

    return ret[0]

quantize(0,s)

print(ret[0])
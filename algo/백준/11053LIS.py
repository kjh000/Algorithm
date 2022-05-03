import sys
import math
import bisect

INF = math.inf

LIS = [-INF]

length = 0

n = int(input())

A = list(map(int,input().split()))

for i in range(n):
    
    idx = bisect.bisect_left(LIS,A[i])
    if idx == len(LIS):
        LIS.append(A[i])
        length += 1
    else:
        if LIS[idx] > A[i]:
            LIS[idx] = A[i]
            
print(length)
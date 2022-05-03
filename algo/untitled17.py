import sys
import math

n=2000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False



def is_Prime(n):
    if(n<2):
        return False
    
    x = math.ceil(n**(0.5))
    
    for i in range(2,x+1):
        if(n%2 == 0):
            return False
        
    return True

def binary_search(lst,key):
    low = 0
    high = len(lst) - 1
    
    
    while high >= low:
        mid = (low + high)//2
        if key < lst[mid]:
            high = mid -1
        elif key == lst[mid]:
            return mid
        else:
            low = mid + 1
            
    return -low -1



N = int(input())
arr = list(map(int,input().split()))


match = [-1]*(2001)

v = {}
ans = 0
one = []

def dfs(here):
    
    if visited[here] != 0:
        return 0
    
    visited[here] = 1
    
    for i in range(len(v[here])):
        work = v[here][i]
        if binary_search(primes,work + here) >= 0:
            
            if(match[work] == -1 or dfs(match[work]) != 0):
                match[work] = here
#                match[here] = work
#                print(here,work)
                return 1
    
    return 0
  
for i in range(N):

    v[arr[i]] = []
    
    for j in range(N):
        if i == j: continue
        v[arr[i]].append(arr[j])
        
for i in range(1,N):
    
    if binary_search(primes,arr[0] + arr[i]) >= 0:
        
        match = [-1]*(2001)
        visited = [0]*(n+1)
        visited[arr[0]] = 1
#        visited[arr[i]] = 1
#        match[arr[0]] = arr[i]
        match[arr[i]] = arr[0]
    
        comp = 2
        for j in range(1,N):
            if i == j: continue
            comp += dfs(arr[j])
            
        if comp == N:
            one.append(arr[i])
one.sort()
if one:
    for i in one:
        print(i,end = ' ')
else:
    print(-1)
    
print()

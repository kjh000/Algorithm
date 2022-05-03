import sys

def isInside(x,y):
    if 0 <= n < m and 0 <= y <m:
        return True
    else:
        return False
        


m,n = map(int,input().split())

mat = [list(map(int,input().split())) for _ in range(m)]


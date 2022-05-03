import sys
import heapq

#T = int(input())

n = int(input())
xy = []
xx = []
yy = {}

kl,kr = 0,0
heap = []
mx,my = 0,0
tot_y = 0

for i in range(n):
    x,y = map(int,input().split())
    xy.append([x,y])
    yy[y] = 0
    xx.append(x)

xy.sort()
xx.sort()

for i in range(n):
    yy[xy[i][1]] += 1

for i in yy:
    tot_y += i*yy[i]
    
    
mean_y = round(tot_y/n)
mean_x = round(sum(xx)/n)

for h in yy:
    tmp = abs(mean_y - h)*yy[h]
    my += tmp
    
for i in xx:
    heapq.heappush(heap,[abs(mean_x - i),i])
    
for i in range(n):
    now = heapq.heappop(heap)
    dis = now[0]
    xc = now[1]
    print(now)
    if xc >= mean_x:
        mx += (dis + kr)
        kr += 1
    else:
         mx += (dis - xc + kl)
         kl += 1
         
ans = mx + my
print(ans)
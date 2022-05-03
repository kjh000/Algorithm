import sys
import math
import bisect


def distance(x1,y1,x2,y2):
    
    dis = (x1-x2)**2 + (y1-y2)**2
    return dis

n = int(input())

x = []
y = []

for i in range(n):
    xi,yi = map(int,input().split())
    
    x.append([xi,yi])
    y.append([yi,xi])
    
x.sort()
y.sort()

def roof(n):
    
    INF = math.inf
    mini = INF

    for i in range(1,n):
        dis = distance(x[0][0],x[0][1],x[i][0],x[i][1])
        mini = min(dis,mini)
        
    
        
    for i in range(1,n):
        
        xbound = x[i][0] + mini**(0.5)
        xcandi = bisect.bisect_left(x,[xbound,INF],i,n)
        
        for j in range(i+1,xcandi):
            xdis = distance(x[i][0],x[i][1],x[j][0],x[j][1])
            mini = min(mini,xdis)
            
        ybound = y[i][0] + mini**(0.5)
        ycandi = bisect.bisect_left(y,[ybound,INF],i,n)
            
        for j in range(i+1,ycandi):
            ydis = distance(y[i][1],y[i][0],y[j][1],y[j][0])
            mini = min(mini,ydis)
           
    return mini

ans = roof(n)
        
print(ans)

 
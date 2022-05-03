import sys

def distance(p1,p2):
    d = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
    return d

def dnq(start,end):
    length = end - start
    if length == 2:
        return distance(points[start],points[start+1])
    if length == 3:
        return min(distance(points[start],points[start+1]),distance(points[start],points[start+2]),distance(points[start+2],points[start+1]))
    else:
        mid = (start + end)//2
        dis = min(dnq(start,mid),dnq(mid,end))
        candi = []
        midx = points[mid][0]
        
        for i in range(start,end):
            if (points[i][0] - midx)**2 <= dis:
                candi.append(points[i])
        c_len = len(candi)
        if c_len >= 2:
            candi.sort(key = lambda x : x[1])
            for i in range(c_len -1):
                for j in range(i+1,c_len):
                    if (candi[i][1] - candi[j][1])**2 > dis:
                        break
                    elif candi[i][0] < midx and candi[j][0] < midx:
                        continue
                    elif candi[i][0] >= midx and candi[j][0] >= midx:
                        continue
                    dis = min(dis,distance(candi[i],candi[j]))
                    
    return dis
    
n = int(input())

points = []

for i in range(n):
    
    x,y = map(int,input().split())
    
    points.append((x,y))

points = list(set(points))    
points.sort()


if n != len(points):
    print(0)
else:
    print(dnq(0,n))
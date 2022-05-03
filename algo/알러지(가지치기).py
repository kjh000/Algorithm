
n,m = map(int,input().split())
name = list(input().split())

name_to_int = {}
food = [[] for _ in range(m)]
canEat = [[] for _ in range(n)]

for ii,nn in enumerate(name):
    name_to_int[nn] = ii
    
for idx in range(m):
    line  = list(input().split())
    fn = int(line[0])
    for jdx in range(fn):
        food[idx].append(name_to_int[line[jdx+1]])
        canEat[name_to_int[line[jdx+1]]].append(idx)
        
best = [m]
edi = [0]*(n+1)

def search(edible,chosen):
    if chosen >= best[0]: return
    first = 0
    while first < n and edible[first] > 0:
        first +=1
        
    if first == n :
        best[0] = chosen
        return
    
    for idx in range(len(canEat[first])):
        food_ = canEat[first][idx]
        for jdx in range(len(food[food_])):
            edible[food[food_][jdx]] += 1
        
        search(edible,chosen+1)
        for jdx in range(len(food[food_])):
            edible[food[food_][jdx]] -= 1
            
search(edi,0)
print(best)
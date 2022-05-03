'''
n : # of objects , w : capacity of pack

pack(capacity,item) : return maximum of sum(eager)
'''

n,w = map(int,input().split())

memo = [[-1]*(n+1) for _ in range(w+1)]

name = [0]*(n)
volume = [0]*(n)
eager = [0]*(n)
picked = []
for i in range(n):
    na,v,e = input().split()
    v,e = int(v),int(e)
    name[i] = na
    volume[i] = v
    eager[i] = e
    
def pack(capacity,item):
    if item == n: return 0
    
    if memo[capacity][item] != -1:
        return memo[capacity][item]
    
    memo[capacity][item] = pack(capacity,item + 1)
    
    if capacity >= volume[item]:
        memo[capacity][item] = max(memo[capacity][item],pack(capacity - volume[item],item + 1) + eager[item])
        
    return memo[capacity][item]

#pack(w,0)
#print(pack(w,0))

def reconstruct(capacity,item,picked):
    if item == n: return
    if pack(capacity,item) == pack(capacity,item + 1):
        reconstruct(capacity,item + 1,picked)
    else:
        picked.append(name[item])
        reconstruct(capacity - volume[item],item + 1,picked)
        
reconstruct(w,0,picked)

print(pack(w,0))
print(picked)
import sys

bias = 4096

class Node(object):
    def __init__(self):
        self.sum = 0
        self.l = 0
        self.r = 0
        self.lr = 0
        
tree = [Node()]*8282

def f(a,b):
    ret = Node()
    ret.sum = a.sum + b.sum
    ret.l = max(a.l,a.sum + b.l)
    ret.r = max(b.r,a.r + b.sum)
    ret.lr = max(a.r + b.l,a.lr,b.lr,ret.sum)
    return ret

def update(x,v):
    x |= bias
    tree[x].sum += v
    tree[x].l += v
    tree[x].r += v
    tree[x].lr += v
    while x :
        tree[x] = f(tree[x<<1], tree[x<<1 | 1])
        x = x >> 1
        
def query(l,r):
    l |= bias
    r |= bias
    ret = Node()
    while(l <= r):
        if l&1:
            l += 1
            ret = f(tree[l],ret)
        if(~r & 1):
            r -= 1
            ret = f(ret,tree[r])
        l = l >> 1
        r = r >> 1
   
    return ret

n = int(input())
mat = []

for i in range(n):
    x,y,w = map(int,input().split())
    update(y,w)
    
ans = [query(0,3)]
print(ans[0].sum)
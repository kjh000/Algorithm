import sys

MAX_N = 30

class Node(object):
    def __init__(self):
        self.lsum = 0
        self.rsum = 0
        self.tsum = 0
        self.msum = 0
        
tree = [0]*(4*MAX_N)
for i in range(4*MAX_N):
    tree[i] = Node()
    
def update(pos,val,node,start,end):
    if end < pos or pos < start:
        return
    if start == end:
        tree[node].tsum += val
        tree[node].lsum += val
        tree[node].rsum += val
        tree[node].msum += val
        return
    
    mid = (start + end)//2
    update(pos,val,node*2,start,mid)
    update(pos,val,node*2 + 1,mid+1,end)
    tree[node].lsum = max(tree[node*2].lsum,tree[node*2].tsum + tree[node*2 + 1].lsum)
    tree[node].rsum = max(tree[node*2 + 1].rsum,tree[node*2 + 1].tsum + tree[node*2].rsum)
    tree[node].tsum = tree[node*2].tsum + tree[node*2 + 1].tsum
    tree[node].msum = max(tree[node*2].rsum + tree[node*2 + 1].lsum,tree[node*2].msum,tree[node*2 + 1].msum,tree[node].lsum,tree[node].rsum)
    
def query(lo,hi,node,start,end):
    if end < lo or hi < end:
        return 0
    if lo <= start and end <= hi:
        return tree[node].msum
    
    mid = (start + end)//2
    return max(query(lo,hi,node*2,start,mid),query(lo,hi,node*2 + 1,mid+1,end))

n = int(input())
ans = 0

for i in range(n):
    x,y,w = map(int,input().split())
    update(y,w,1,0,3)
    q = query(0,3,1,0,3)
    ans = max(q,ans)
    
print(ans)
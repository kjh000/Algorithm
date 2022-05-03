
INF = 10**9 + 1

a = [5,3,3,4,5,2]

n = len(a)
tree = [0]*(n*4)

def init(array,left,right,node):
    if left == right:
        tree[node] = array[left]
        return tree[node]
    mid = (left + right)//2
    leftMin = init(array,left,mid,node*2)
    rightMin = init(array,mid+1,right,node*2 + 1)
    
    tree[node] = min(leftMin,rightMin)
    return tree[node]

init(a,0,5,1)


def query(left,right,node,nodeLeft,nodeRight):
    if right < nodeLeft or nodeRight < left: return INF
    if left <= nodeLeft and nodeRight <= right:
        return tree[node]
    
    mid = (nodeLeft + nodeRight)//2
    return min(query(left,right,node*2,nodeLeft,mid),query(left,right,node*2 + 1,mid+1,nodeRight))

def update(idx,value,node,nodeLeft,nodeRight):
    if idx < nodeLeft or nodeRight < idx:
        return tree[node]
    if nodeLeft == nodeRight:
        tree[node] = value
        return tree[node]
    
    mid = (nodeLeft + nodeRight)//2
    tree[node] = min(update(idx,value,node*2,nodeLeft,mid),update(idx,value,node*2+1,mid+1,nodeRight))
    return tree[node]

#class RangeResult(object):
#    def __init__(self):
#        self.size = None
#        self.mostFrequent = None
    
print(query(0,5,1,0,n-1))
update(0,1,1,0,n-1)
print(query(0,5,1,0,n-1))
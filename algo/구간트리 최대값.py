"""

"""


INF = 10**9 + 1

a = [7,2,3,4,5,6]

n = len(a)
tree = [0]*(n*4)

def init(array,left,right,node):
    if left == right:
        tree[node] = array[left]
        return tree[node]
    mid = (left + right)//2
    leftMax = init(array,left,mid,node*2)
    rightMax = init(array,mid+1,right,node*2 + 1)
    
    tree[node] = max(leftMax,rightMax)
    return tree[node]

init(a,0,5,1)


def query(left,right,node,nodeLeft,nodeRight):
    if right < nodeLeft or nodeRight < left: return -INF
    if left <= nodeLeft and nodeRight <= right:
        return tree[node]
    
    mid = (nodeLeft + nodeRight)//2
    return max(query(left,right,node*2,nodeLeft,mid),query(left,right,node*2 + 1,mid+1,nodeRight))

def update(idx,value,node,nodeLeft,nodeRight):
    if idx < nodeLeft or nodeRight < idx:
        return tree[node]
    if nodeLeft == nodeRight:
        tree[node] = value
        return tree[node]
    
    mid = (nodeLeft + nodeRight)//2
    tree[node] = max(update(idx,value,node*2,nodeLeft,mid),update(idx,value,node*2+1,mid+1,nodeRight))
    return tree[node]

#class RangeResult(object):
#    def __init__(self):
#        self.size = None
#        self.mostFrequent = None
    
#print(query(5,5,1,0,n-1))
print(query(0,2,1,0,n-1))
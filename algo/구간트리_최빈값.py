
INF = 10**9 + 1

class RangeResult(object):
    def __init__(self,v):
        self.size = 1
        self.mostFrequent = 1
        self.leftNumber = v
        self.leftFreq = 1
        self.rightNumber = v
        self.rightFreq = 1
        
#arr = [1,1,1,4,4,5]
arr = [RangeResult(1),RangeResult(1),RangeResult(1),RangeResult(4),RangeResult(4),RangeResult(5)]

n = len(arr)


        
tree = [RangeResult(0)]*(n*4)

### a,b : object of RangeResult
def merge(a,b):
#    a = arr[a]
#    b = arr[b]
    ret = RangeResult(0)
    ret.size = a.size + b.size
    ret.leftNumber = a.leftNumber
    ret.leftFreq = a.leftFreq
    if a.size == a.leftFreq and a.leftNumber == b.leftNumber:
        ret.leftFreq += b.leftFreq
        
    ret.rightNumber = b.rightNumber
    ret.rightFreq = b.rightFreq
    if b.size == b.rightFreq and a.rightNumber == b.rightNumber:
        ret.rightFreq += a.rightFreq
        
    ret.mostFrequent = max(ret.mostFrequent,a.rightFreq + b.leftFreq)
    
    return ret

def init(array,left,right,node):
    if left == right:
        tree[node] = arr[left]
#        tree[node].leftNumber = left
#        tree[node].rightNumber = right
        
        return tree[node]
    
    mid = (left + right)//2
    leftMin = init(array,left,mid,node*2)
    rightMin = init(array,mid+1,right,node*2 + 1)
    
    tree[node] = merge(leftMin,rightMin)
    return tree[node]

init(arr,0,5,1)


def query(left,right,node,nodeLeft,nodeRight):
    if right < nodeLeft or nodeRight < left: return INF
    if left <= nodeLeft and nodeRight <= right:
        return tree[node]
    
    mid = (nodeLeft + nodeRight)//2
    return merge(query(left,right,node*2,nodeLeft,mid),query(left,right,node*2 + 1,mid+1,nodeRight))

def update(idx,value,node,nodeLeft,nodeRight):
    if idx < nodeLeft or nodeRight < idx:
        return tree[node]
    if nodeLeft == nodeRight:
        tree[node] = value
        return tree[node]
    
    mid = (nodeLeft + nodeRight)//2
    tree[node] = merge(update(idx,value,node*2,nodeLeft,mid),update(idx,value,node*2+1,mid+1,nodeRight))
    return tree[node]

        
print(query(1,6,1,0,n-1))
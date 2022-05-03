
class Node(object):
    def __init__(self,l,r,v):
        self.left = l
        self.right = r
        self.val = v
        
node = [None]*2

node[0] = Node(0,0,0)
node[1] = Node(0,0,0)

def upd(i,x,nidx,node_start,node_end):
    if i < node_start or i > node_end: return
    node[nidx].val += x
    if node_start != node_end : 
        mid = (node_start + node_end)//2
        if i <= mid:
            if node[nidx].left == 0:
                node.append(Node(0,0,0))
                node[nidx].left = len(node) - 1
            upd(i,x,node[nidx].left,node_start,mid)
        else:
            if node[nidx].right == 0 :
                node.append(Node(0,0,0))
                node[nidx].right = len(node) - 1
                
            upd(i,x,node[nidx].right,mid + 1,node_end)
            
def update(i,x):
    upd(i,x,1,1,10**9 -1)

def qry(i,j,nidx,node_start,node_end):
    if j <node_start or i > node_end : return 0
    elif i <=node_start and j>= node_end : return node[nidx].val

    mid = (node_start + node_end)//2
    ret = 0
    if i <= mid:
        if node[nidx] == 0:
            node.append(Node(0,0,0))
            node[nidx].left = len(node) - 1
        ret += qry(i,j,node[nidx].left,node_start,mid)

    if j >= mid + 1:
        if node[nidx].right == 0:
            node.append(Node(0,0,0))
            node[nidx].right = len(node) - 1
        ret += qry(i,j,node[nidx].right,mid+1,node_end)
        
    return ret

def query(i,j):
    return qry(i,j,1,1,10**9 -1 )


update(2,10)
update(3,14)

print(query(1,3))
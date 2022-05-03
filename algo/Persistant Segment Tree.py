'''
example for BAEK 11012
head[i] : root of  ith segment tree

node[0] : dummy node , node[1] = root
10**5 : boundary of dimension
yidx : (x,y) --> yidx[x] = [y]
n : number of points
'''

class Node(object):
    def __init__(self,l,r,val):
        self.l = l
        self.r = r
        self.val = val
        
head = [0]*100002
node = [Node(0,0,0),Node(0,0,0)]

def init(nidx,node_st,node_end):
    if node_st == node_end: return
    mid = (node_st + node_end)//2
    node.append(Node(0,0,0))
    node[nidx].l = len(node) - 1
    init(node[nidx].l,node_st,mid)
    node.append(Node(0,0,0))
    node[nidx].r = len(node) - 1
    init(node[nidx].r,node_st,mid)
    
    
def upd(i,x,nidx,node_st,node_end):
    if node_st == node_end : return
    mid = (node_st + node_end)//2
    if i <= mid:
        lidx = node[nidx].l
        node.append(Node(node[lidx].l,node[lidx].r,node[lidx].val + x))
        node[nidx].l = len(node) - 1
        upd(i,x,node[nidx].l, node_st,mid)
        
    else:
        ridx = node[nidx].r
        node.append(Node(node[ridx].l,node[ridx].r,node[ridx].val +x))
        node[nidx].r = len(node) - 1
        upd(i,x,node[nidx].r,mid+1,node_end)
        
        
def query(i,j,nidx,node_st,node_end):
    if j < node_st or i > node_end : return 0
    elif i <= node_st and node_end <= j : return node[nidx].val 
    mid = (node_st + node_end)//2
    
    ret = query(i,j,node[nidx].l,node_st,mid) + query(i,j,node[nidx].r,mid+1,node_end)
    
    return ret

def heading(head,node,yidx):
    
    for i in range(1,100002):
        if head[i] == 0:
            node.append(Node(node[head[i-1]].l,node[head[i-1]].r,node[head[i-1]].val))
            head[i] = len(node)-1
        
        for y in yidx[i]:
            node[head[i]].val += 1
            upd(y,1,head[i],1,100001)
        

        
            

T = int(input())

for tt in range(T):
    
    head = [0]*100002
    node = [Node(0,0,0),Node(0,0,0)]
    node[1] = Node(0,0,0)
    head[0] = 1
    init(1,1,100001)
    yidx = [[] for _ in range(100002)]
    
    n,m = map(int,input().split())
    total = 0
    for i in range(n):
        x,y = map(int,input().split())
        yidx[x+1].append(y+1)
#    
#    for i in range(1,100002):
#        if head[i] == 0:
#            node.append(Node(node[head[i-1]].l,node[head[i-1]].r,node[head[i-1]].val))
#            head[i] = len(node)-1
#        
#        for y in yidx[i]:
#            node[head[i]].val += 1
#            upd(y,1,head[i],1,100001)

    heading(head,node,yidx)
    for i in range(m):
        l,r,b,t = map(int,input().split())
        
        total += query(b+1,t+1,head[r+1],1,100001) - query(b+1,t+1,head[l],1,100001)
        
    print(total)
            
    node.clear()
            
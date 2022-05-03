import sys

sys.setrecursionlimit(10**6)

def build(arr,v,start,end):
    
    if (start == end):
        
        tree[v] = start

    else:
        mid = (start + end)//2
        build(arr,v*2, start,mid)
        
        build(arr,v*2 + 1,mid+1,end)
        if arr[tree[2*v]] >= arr[tree[2*v+1]]:
            tree[v] = tree[2*v+1]
        else:
            tree[v] = tree[2*v]
    return tree


def range_minimum_query(node, segx, segy, qx, qy):
    
    if qx > segy or qy < segx:      
        return 10**9 + 7
    elif segx >= qx and segy <= qy:  
        return tree[node]
    
    left = range_minimum_query(node*2, segx, (segx + segy)//2, qx, qy)
    right = range_minimum_query(node*2 + 1, ((segx + segy)//2) + 1, segy, qx, qy)
    
    if  left >= 10**9 + 7 :  return right
    elif right >= 10**9 +7: return left
    else:
        if arr[left] < arr[right]:
            return left
        else:
            return right

while 1:
    tree = [0]*300000

    mat = list(map(int,input().split()))
    n = mat[0]
    if n == 0: break
    arr = mat[1:]
    
    build(arr,1,0,n-1)
    
    ans = []
    def binary_search(lo,hi):
    
        if lo == hi:
            ans.append(arr[lo-1])
            return
        
        mid = range_minimum_query(1,1,n,lo,hi)
        ans.append(arr[mid]*(hi-lo+1))
        if mid == lo -1:
            binary_search(mid+2,hi)
        elif mid == hi -1:
            binary_search(lo,mid)
        else:
            binary_search(lo,mid)
            binary_search(mid+2,hi)
    
        
    binary_search(1,n)
    print(max(ans))
    
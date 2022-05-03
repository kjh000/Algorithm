import sys

T = int(input())

for t in range(T):
    n = int(input())
    
    mat = []
    ans = 0
    
    ori = []
    zip = {}
    
    for i in range(n):
        x,y = map(int,input().split())
        mat.append([x,y])
#        ori.append(x)
        ori.append(y)
    
        
    mat.sort(key = lambda x : (x[0],-x[1]))
    
    ori = list(set(ori))
    ori.sort()
    
    for idx,num in enumerate(ori):
        zip[num] = idx+1
        
    for point in mat:
#        point[0] = zip[point[0]]
        point[1] = zip[point[1]]
        
    N = n+10
    tadd = [0]*(N+1)
    tmul = [0]*(N+1)
    
    def inupadate(at,mul,add):
        if(at<1 or at>N): return

            
        while(at<=N):
            tmul[at] += mul
            tadd[at] += add
            
            at += at&-at
            
    def range_update(l,r,by):
        inupadate(l,by,-by*(l-1))
        inupadate(r+1,-by,by*r)
        
    def range_query(at):
        if(at==0): return 0
        if(at<1 or at>N): return 
        
        mul,add = 0,0
        
        i = at
        while i>0:
            mul +=tmul[i]
            add += tadd[i]
            i -= i&-i
    
        return at*mul + add
    
    for i in range(n):
        node = mat[i][1]
        if i == 0:
            range_update(node,node,1)
        else:
            ans += range_query(N) - range_query(node-1)
            range_update(node,node,1)
            
    print(ans)
            
        
        
        
        
        
        
        
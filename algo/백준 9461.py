








T = int(input())

for t in range(T):
    
    N = int(input())
    
    
    up = [1,1,2,4]
    down = [1,2,3,5]
    
    mat = []
    
    
    for i in range(51):
        up.append(0)
        down.append(0)
    
    
    for i in range(4,51):
    
        up[i] = down[i-1]+down[i-3]
        down[i] = up[i] + up[i-2]
        
    #    
    for i in range(51):
        mat.append(up[i])
        mat.append(down[i])
        
        
    print(mat[N-1])
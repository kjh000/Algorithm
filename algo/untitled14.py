import sys

def isSquare(num):
    
    if num == 0:
        return 1
    
    if num < 0:
        return -1
    else:
            
        tmp = num**(0.5)
    
        
        if int(tmp) == tmp:
            return 1
        else:
            return -1

T = int(input())
        
for t in range(T):
    n = int(input())
    
    mat = list(map(int,input().split()))
    ans = [0]
    
    def roof(n):
        
        for i in range(n):
            total = 0
            for j in range(i,n):
               
                total += mat[j]
                if isSquare(total) == 1:
                   
                    ans[0] += 1    
                    
                    
    roof(n)
    print('Case #{}: {}'.format(t+1,ans[0]))
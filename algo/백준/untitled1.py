import sys


N = int(input())
cols = [0]*N
ans = [0]

def back_tracking(level):
    
    if level == N:
#        print(cols)
        ans[0] += 1
        
    else:
        for i in range(N):
            cols[level] = i
            if isPossible(level):
                back_tracking(level + 1)
                
    
def isPossible(level):
    for i in range(level):
        
        if cols[i] == cols[level] or abs(level - i) == abs(cols[level]-cols[i]):
            return False
        
    return True


back_tracking(0)


print(ans)
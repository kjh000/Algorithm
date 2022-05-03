import sys


  
def near(n):
    
    for i in range(31):
        if n >= 2**i: pass
        else:
            nn = i-1
            break
    return 2**nn

def binary_search(lst,key):
    low = 0
    high = len(lst) - 1
    
    
    while high >= low:
        mid = (low + high)//2
        if key < lst[mid]:
            high = mid -1
        elif key == lst[mid]:
            return mid
        else:
            low = mid + 1
            
    return -low -1
    
def check(num):
    for i in sum_e:
        if i <= 1: pass
        else:    
            if num%i == 0:
                return True
            
    return False

sum_e = []

for i in range(31):
    sum_e.append(2**i - 1)
    
jn = [0]
def search(x):
    
    idx = binary_search(sum_e,x)
    
    if idx >= 0:
        jn[0] += idx
        x += sum_e[idx]
        return 
    
    else:
        idx = -idx -2
        jn[0] += idx
        x -= sum_e[idx]
        search(x)
T = int(input())
for t in range(T):
    
    jn = [0]
    x,y = map(int,input().split())
    
    candidates = []
    xi = binary_search(sum_e,x)
    yi = binary_search(sum_e,y)
    
    search(x)
    jx = jn[0]
    jn = [0]
    search(y)
    jy = jn[0]
    jn = [0]
    candidates.append(jx)
    candidates.append(jy)
    
    
    x_base = 0
    if xi < 0 :
        x_base = sum_e[-xi - 2]
    else:
        x_base = sum_e[xi - 1]
        
    y_base = 0
    if yi < 0 :
        y_base = sum_e[-yi - 2]
    else:
        y_base = sum_e[yi - 1]
    
    if y_base > x_base:
        ne = near(y_base - x_base)    
        
    
    
    

import sys


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
    cnt = 0
    
    while 1:
        if num%2 == 1:
            cnt += 1
            num = (num-1)//2
        else:
            num = num//2 
        
        if num == 0:
            break
    
    if cnt%2 == 0:
        return 0
    else: return 1

T = int(input())

for t in range(T):
    n,q = map(int,input().split())
    
    mat = list(map(int,input().split()))
    bit_mat = []
    ans = []
    one = []
    
    for idx,a in enumerate(mat):
        b = check(a)
        bit_mat.append(b)
    
        if b == 1:
            one.append(idx)
    if one:
        first_one = one[0]
        last_one = one[-1]
    else:
        first_one = n
        last_one = 0
    tot = sum(bit_mat)
    
    
    for i in range(q):
        p,v = map(int,input().split())
        
        v = check(v)
        tot -= bit_mat[p]
        
        if v == 1 and bit_mat[p] == 0:
            k = binary_search(one,p)
            one.insert(-k-1,p)
            first_one = one[0]
            last_one = one[-1]
        elif v == 0 and bit_mat[p] == 1:
            one.remove(p)
            if one:
                first_one = one[0]
                last_one = one[-1]
            else:
                first_one = n
                last_one = 0
        
        bit_mat[p] = v
        tot += v
        
    
        if tot%2 == 0: ans.append(n)
        else:
            ans.append(max(last_one,n-first_one-1))
        
        
    print('Case #{}:'.format(t+1),end = ' ')
    for i in ans:
        print(i,end = ' ')
        
        
    print('')
    sys.stdout.flush()
        
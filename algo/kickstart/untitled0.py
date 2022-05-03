import sys
T = int(input())

for t in range(T):
    
    N = int(input())
    
#    s = input()
    s = sys.stdin.readline()
    

    last = 1
    
 
    ss = '1'
    
    for i in range(1,N):
        
        if ord(s[i]) > ord(s[i-1]):
            last += 1
            
        else:
            last = 1
            
        ss = ss + ' ' + str(last)
    
    
    print('Case #{}: {}'.format(t+1,ss))
          
import sys

while True:
    try:
        N = 100100
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
        
        n,k = map(int,input().split())
        
        mat = list(map(int,input().split()))
        ans = []
        
        for i in range(n):
            
            x = mat[i]
            if(x < 0):
                range_update(i+1,i+1,1)
            elif(x > 0):
                range_update(i+1,i+1,0)
            else:
                range_update(i+1,i+1,-(10**5 + 1))
        
        for i in range(k):
            order = list(input().split())
            a,b = int(order[1]),int(order[2])
            if(order[0] == 'C'):
                aa = range_query(a) - range_query(a-1)
                if(aa == 0):
                    
                    if(b < 0):
                        range_update(a,a,1)
                    elif(b > 0):
                        range_update(a,a,0)
                    else:
                        range_update(a,a,-(10**5 + 1))
                        
                elif(aa == 1):
                    
                
                    if(b < 0):
                        range_update(a,a,0)
                    elif(b > 0):
                        range_update(a,a,-1)
                    else:
                        range_update(a,a,-1-(10**5 + 1))
                else:
                
                    if(b < 0):
                        range_update(a,a,1 + 10**5 + 1)
                    elif(b > 0):
                        range_update(a,a,10**5 + 1)
                    else:
                        range_update(a,a,0)
                
            else:
                tmp = range_query(b) - range_query(a-1)
                if(tmp > 0):
                    if(tmp%2 == 0):
                        ans.append('+')
                    else:
                        ans.append('-')
                    
                    
                elif tmp == 0 : 
                    ans.append('+')
                else:
                    ans.append('0')
        
        
        print(''.join(ans))
    except :
        break
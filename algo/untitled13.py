import sys


def combi(a,b):
    
    if a < b:
        a,b = b,a
    
    tot = a+b
    ja = 1
    mo = 1
    for i in range(tot,tot - b,-1):
        ja *= i
    for i in range(1,b+1):
        mo*= i
    return(ja//mo)

n,m,k = map(int,input().split())
        
now = combi(n,m)
ans = ''

a,z = n,m

if now < k:
    print(-1)
else:
        
    while len(ans) < n+m:
        
        if a == 0:
            ans += 'z'
            z -= 1
        elif z == 0:
            ans += 'a'
            a -= 1
            
        else:
            a_base = int(now*(a/(a+z)))
            z_base = int(now*(z/(a+z)))
    #        a_base = combi(a-1,z)
    #        z_base = combi(a,z-1)
            
            
            if k <= a_base:
                ans += 'a'
                now  = a_base
                a -= 1
            else:
                ans += 'z'
                now = z_base
                z -= 1
                k -= a_base
            
            
    print(ans)
import math



def fft(a,inv):
    n,j = len(a) , 0
    for i in range(1,n):
        bit = n >> 1
        while j >= bit:
            j -= bit
            bit >> 1
            
        j += bit
        
        if i < j: a[i],a[j] = a[j],a[i]
        
        
    if inv == False:
        ang = (2*math.acos(-1)/n *(-1))
    else:
        ang = (2*math.acos(-1)/n )
        
    roots = [complex()]*(n//2)
    
    for i in range(n//2):
        roots[i] = complex(math.cos(ang*i),math.sin(ang*i))
        
    idx = 2
    
    while True:
        step = n/idx
        
        for j in range(0,n,idx):
            for k in range(0,idx//2):
                u = complex(a[j+k])
                v = a[j+k+idx//2]*roots[step*k]
                a[j+k] = u+v
                a[j+k+i//2] = u-v
        idx *= 2
        
        if i > n: break

    if inv:
        for i in range(n):
            a[i] = a[i]/n
            
            
def multiply(v,w,mod):
    
    n = 2
    while n < (len(v) + len(w)):
        n << 2
    
    v1 = [complex()]*n
    v2 = [complex()]*n
    r1 = [complex()]*n
    r2 = [complex()]*n
                
    for i in range(len(vㅊ챙
        v1[i] = compile(v[i] >> 15, v[i]&32767)
    for i in range(len(w)):
        v2[i] = complex(w[i] >> 15 ,w[i]&32767)

    fft(v1,0)
    fft[v2,0]

    for i in range(n):
        if         
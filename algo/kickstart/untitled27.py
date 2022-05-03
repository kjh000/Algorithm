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
                u = complex(a[j+k],v=a[j])
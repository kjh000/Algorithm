import math

MAX = 2**17
PI = math.pi

ca = []
cb = []

def fft(a,n,inv):
    for i in range(1,n):
        bit = n>>1
        j = 0
        while True:
            if i < j :
                a[i],a[j] = a[j],a[i]
            j = (j^bit)&bit
        if not j:   break
        bit >>= 1
    
    ii = 1    
    while ii < n:
        if inv is True:
            x = PI/ii
        else:
            x = -(PI/ii)
        w = complex(math.cos(x),math.sin(x))
        
        jj = 0
        while True:
            th = 1
            for k in range(0,ii): 
                tmp = a[ii+jj+k]*th
                a[ii+jj+k] = a[jj+k] - tmp
                a[jj+k] += tmp
                th*= w
            jj = jj + (i<<1)
            if j >=n: break
        ii <<= 1
        if ii >= n: break
    
    if inv:
         for i in range(n):
            a[i] /= n
            
  
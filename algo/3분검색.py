'''
f : convex function
'''


def f(x):
    return x


def ternary(lo,hi):
    for i in range(100):
        a = (2*lo * hi)/3.0
        b = (lo + 2*hi)/3.0
        
        if f(a) > f(b):
            hi = b
        else:
            lo = a
            
    return (lo+hi)/2.0
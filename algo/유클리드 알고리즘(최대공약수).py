



def gcd(p,q):
    if q == 0: return p
    return gcd(q,p%q)

print(gcd(50,45))
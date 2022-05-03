'''
N : original string
H : string to find

return = start index
'''


def getPartialMatch(N):
    
    m = len(N)
    pi = [0]*m

    begin , matched = 1,0

    while begin + matched < m:
        if N[begin + matched] == N[matched]:
            matched += 1
            pi[begin + matched -1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched -1]
                matched = pi[matched - 1]
        
    return pi

def kmpSearch(H,N):
    n = len(H)
    m = len(N)
    ret = []
    pi = getPartialMatch(N)

    begin,matched = 0,0
    
    while begin <= n-m:
        if matched < m and H[begin + matched] == N[matched]:
            matched += 1
            
            if matched == m : ret.append(begin)
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched-1]
                
                matched = pi[matched -1]
                
    return ret



a = kmpSearch('AKICKSTARTPROBLEMNAMEDKICKSTART','KICK')
print(a)
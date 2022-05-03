

n = 7
Edge = {1 : [2,3], 2: [4,5], 3:[6,7],4:[],5:[],6:[],7:[]}

visit = [0]*(n+1)

def dfs(here):
    
    print('visit {}'.format(here))
    
    visit[here] = 1
    
    for i in Edge[here]:
        there = i
        if visit[there] == 0:
            dfs(there)
            
def dfsAll():

    for i in range(1,n+1):
        if visit[i] == 0:
            dfs(i)
            
dfsAll()
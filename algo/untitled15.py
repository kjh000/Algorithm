import sys
import queue
T = int(input())
for t in range(T):
    r,c = map(int,input().split())
    
    mat = [ input() for _ in range(r)]
    
    visit = [0]*26
    below = {}
    indegree = {}
    q = queue.Queue()
    result = ''
    
    for i in range(r):
        for j in range(c):
            below[mat[i][j]] = []
            indegree[mat[i][j]] = 0
            
    for i in range(1,r):
        for j in range(c):
            if mat[i][j] != mat[i-1][j]:
                below[mat[i][j]].append(mat[i-1][j])
            
    for i in below:
        below[i] = list(set(below[i]))
        
    for i in below:
        for j in below[i]:
            indegree[j] += 1
            
    for i in below:
        if indegree[i] == 0:
            q.put(i)
            
#    print(below)
    
    while not q.empty():
        
         cur = q.get()
         result += cur
         
         for i in below[cur]:
             
             indegree[i] -= 1
             if(indegree[i] == 0):
                 q.put(i)
                 
    if result:
        print('Case #{}: {}'.format(t+1,result))
    else:
        
        print('Case #{}: -1'.format(t+1))
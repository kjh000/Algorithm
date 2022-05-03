import sys

n,m = map(int,input().split())

student = [[] for _ in range(n+1)]

indegree = [0]*(n+1)

q = []
result = []


for i in range(m):
    a,b = map(int,input().split())
#    a,b = map(int,sys.stdin.readline().split())
    
    indegree[b] += 1
    
    student[a].append(b)
    

for i in range(1,n+1):
    
    if(indegree[i] == 0):
        q.append(i)
   
    
while q:
    
     cur = q.pop()
     result.append(cur)
     
     for i in student[cur]:
         
         indegree[i] -= 1
         if(indegree[i] == 0):
             q.append(i)
             

for i in range(n):
    
    print(result[i],end = ' ')
             
#print(result)
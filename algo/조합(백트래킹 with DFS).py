'''
MAX = # of array
'''


MAX = 5

arr = list(map(int,input().split()))
select = [False]*MAX


def pprint():
    for i in range(MAX):
        if select[i]:
            print(arr[i],end = ' ')
    print()

def dfs(idx,cnt,limit):
    
    if cnt == limit:
        pprint()
        return

    for i in range(idx,MAX):
        if select[i]: continue
        select[i] = True
        
        dfs(i,cnt+1,limit)
        select[i] = False
        
        
dfs(0,0,3)


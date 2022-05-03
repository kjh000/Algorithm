import bisect
import math

#a = [1,3,5,7,9]
#
#b = [2,4,6,8,10,12]
#
#c = [[1,2],[2,1],[3,4],[4,4]]
#
#
#print(bisect.bisect_left(a,7))
#print(bisect.bisect_right(a,7))
#
#print(bisect.bisect_left(b,5))
#
#print(bisect.bisect(b,5))
#print(bisect.bisect_left(c,[2,2]))

#
#mat = [0]*5
#arr = [0]
#def dfs(a):
#    if a == 5: return
#    arr[0] += 1
#    dfs(a+1)
#    
#    mat[a] = arr[0]
#    
#dfs(0)
#
#print(mat)


#a = [4,2,1,3,4]
#
#b = sorted(a)
#
#print(a)



#mat = [[1,2],[4,3],[2,2],[3,6]]
#xmat = sorted(mat,key = lambda  mat : mat[0])
#ymat = sorted(mat,key = lambda  mat : mat[1])

#print(math.ceil(0.5))

#a = False
#
#if a :
#    print('True')
#else:
#    print('False')
#
#a = [0]
#
#def go(n):
#    if n < 5:
#        go(n+1)
##        return
#        
#    a[0] = n
#    
#
#go(0)
#print(a)
#a = [1,2,3,4]
#print(a[-4])

#a = [[2,3],[1,4],[1,1],[3,2]]
#
#a.sort(key = lambda x : (x[0],-x[1]))
#
#print(a)

#print(-2**(0.5))

#print(int(a))

#c = '-_.~!@#$%^&*()=+[{]}:?,<>'
#
#a = ['a', 'a', 'a', 'a', '+', '+', ';', ';']
#a.pop(6)
#print(a)

#def ranges(nums):
#    nums = sorted(set(nums))
#    gaps = [[s, e] for s, e in zip(nums, nums[1:]) if s+1 < e]
#    edges = iter(nums[:1] + sum(gaps, []) + nums[-1:])
#    return list(zip(edges, edges))

#a = 'asv asdf'
#b = a.split(' ')
#print(b)
#a = [1,2,3,4]
#a[1],a[2] = a[2],a[1]
#
#print(a)
#y = [0]*(3+1)
#print(y)
#
#def exmp(idx):
#    return idx
#
#a = exmp(1)
#print(a)
#def time_gap(t1,t2):
#    t1 = t1.split(':')
#    t2 = t2.split(':')
#    
#    minutes1 = int(t1[0])*60 + int(t1[1])
#    minutes2 = int(t2[0])*60 + int(t2[1])
#    
#    return minutes2 - minutes1
#
#a = time_gap('06:00','7:31')
#print(a)

a = 1

print(a)

a = str(a)

print(a)
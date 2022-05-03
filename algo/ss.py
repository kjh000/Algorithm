import bisect

a = [1,3,5,5,6,7,9,11,13,15]

print(bisect.bisect_left(a,6,0,8))
print(bisect.bisect_right(a,6,0,8))
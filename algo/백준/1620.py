import sys

n,m = map(int,input().split())

digit = ['1','2','3','4','5','6','7','8','9']
char_to_num = {}
num_to_char = []


for i in range(n):
    poketmon = str(input()).strip()
    char_to_num[poketmon] = i+1
    num_to_char.append(poketmon)
    
for i in range(m):
    q = str(input()).strip()
    
    bias = q[0]
    if bias in digit:
        qq = int(q)
        ans = num_to_char[qq-1]
        
    else:
        ans = char_to_num[q]
        
    print(ans)
    
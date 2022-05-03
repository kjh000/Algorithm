'''
add(a,b) : a|b 
intersection(a,b) : a&b
removed(a,b) : a&~b
toggled(a,b) : a^b
first 1 = a&-a
delete fisrt 1 : a &= a-1
'''
arr = [1,3,4,7]

bit_arr = 0

for i in arr:
    bit_arr += 1 <<(i-1)
    
print(bin(bit_arr))
    
p = 3
## check if p in arr
if bit_arr & (1 << p ):
    print('p is in the arr')
else:
    print('no')
    
## delete p
bit_arr &= ~(1<<p-1)

print(bin(bit_arr))

## add p 
bit_arr |= (1<<p-1)

print(bin(bit_arr))

## toggle p
bit_arr ^= (1<<p-1)


subset = bit_arr
while subset > 0:
    visit = (subset - 1)&bit_arr
    print(bin(visit))
    subset = visit
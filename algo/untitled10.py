import sys


BIG = 10**9

vect = ['N','S','E','W']
bracket = ['(',')']
digit = ['2','3','4','5','6','7','8','9']

#T = int(input())

x,y = 1,1
open = 0
xmove, ymove = 0,0

order = input()
in_stack = []
out_stack = []

for node in order:
    if node in vect:
        if node == 'N': ymove -= 1
        elif node == 'S': ymove += 1
        elif node == 'W' : xmove -= 1
        elif node == 'E' : xmove += 1
        
    elif node != ')':
        in_stack.append(node)
        
    elif node == ')':
        xtmp,ytmp = 0,0
        while True:
            cur = in_stack.pop()
            if cur =='(':
                break
            
            if cur == 'N': ytmp -= 1                
            elif cur == 'S': ytmp += 1
            elif cur == 'W': xtmp -= 1
            elif cur == 'E': xtmp += 1
            
        mul = int(in_stack.pop())
        
        xtmp *= mul
        ytmp *= mul
        
        xmove += xtmp
        ymove += ytmp

print(xmove,ymove)
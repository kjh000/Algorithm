# -*- coding: utf-8 -*-
"""
Created on Thu May 16 15:22:00 2019

@author: kjh1
"""

#n = int(input())
n = 4
num = [1,2,3,4]

tree1 = [0]*(n+1)
tree2 = [0]*(n+1)
#tree2 = [0,0,3,9,30]
#tree2 = [0,0,5,13,42]
#tree2 = [0,0,3]
def update_tree(x,v1,v2):
    while(x<= n):
        tree1[x] += v1
        tree2[x] += v2
        
        x += (x&-x)
        
def update(x,y,v):
    update_tree(x,v,(x-1)*v)
    update_tree(y+1,-v,y*(-v))
    

def sumation(x):
    
    t ,tot1,tot2 = x,0,0
    
    while(t>0):
        tot1 += tree1[t]
        tot2 += tree2[t]
#        print(tot1)
#        print(tot2)
        
        t -= t&(-t)
        
    return tot1*x - tot2



#for i in range(n):
#    update_tree(i+1,num[i],i*num[i])
#   



for i in range(1,n+1):
    if(i == 1):
        update_tree(i,num[i-1],0)
        
        a = num[0]+num[1]
        b = num[0]+num[1]
#    elif(i == 2):
#        update_tree(i,num[i-1],a)
#        a += b +3
    else:
        update_tree(i,num[i-1],a)
        
        b += 3
        a += b


    
    
#update_tree(1,num[1-1],0)
#update_tree(2,num[2-1],3)
#update_tree(3,num[3-1],9)
#update_tree(4,num[4-1],18)
#update_tree(5,num[5-1],30)
#
#update_tree(1,num[1-1],0)
#update_tree(2,num[2-1],5)
#update_tree(3,num[3-1],13)
#update_tree(4,num[4-1],24)
#update_tree(5,num[5-1],38)


print(tree1)
print(tree2)

update(2,3,1)
#
#print(tree1)
#print(tree2)
#print(sumation(4))

for i in range(1,n+1):
    print(sumation(i))
#    
#update(1,3,1)
#print(tree1)
#print(tree2)
#
#for i in range(1,n+1):
#    print(sumation(i))
#    
#

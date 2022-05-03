import sys


class Node(object):
    def __init__(self,num):
        self.val = num
        self.level = 0
        self.left = None
        self.right = None
        
    def addNode(self,num):
        
        if self.val > num:
            if self.right:
                self.right.addNode(num)   
            else:
                self.right = Node(num)
                self.right.level = self.level + 1
                nodeLevel[self.level + 1].append(num)
        else:
             if self.left:
                 self.left.addNode(num)
             else:
                 self.left = Node(num)
                 self.left.level = self.level + 1
                 nodeLevel[self.level + 1].append(num)

n = int(input())
nodes = [0]*n
nodeLevel = {}
mat = []
for i in range(n):
    nodeLevel[i] = []
    v = int(input())
    nodes[i] = Node(v)
    mat.append(v)
    
mat.sort()



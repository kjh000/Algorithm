import sys
import collections

Interval = collections.namedtuple('Interval',['lo','hi'])

class ITNode(object):
    def __init__(self,Interval):
        self.i = Interval
        self.maxi = Interval.hi
        self.left = None
        self.right = None
        
class ITree(object):
    def __init__(self):
        self.head = None
        
    def insertion(self,node):
        if self.head ==None:
            self.head = node
            
        else:
            if self.head.maxi < node.i.hi:
                self.head.maxi = node.i.hi
            self.__insertion(self.head,node)
                
    def __insertion(self,head,node):
        if node.i.lo < head.i.lo:
            if head.left == None:
                head.left = node
            else:
                if head.left.maxi < node.i.hi:
                    head.left.maxi = node.i.hi
                self.__insertion(head.left,node)
        else:
            if head.right == None:
                head.right = node
            else:
                if head.right.maxi < node.i.hi:
                    head.right.maxi = node.i.hi
                self.__insertion(head.right,node)
                
    def doOverlab(self,i1,i2):
        return self.__doOverlab(i1,i2)
    
    def __doOverlab(self,i1,i2):
        if i1.lo <= i2.hi and i2.lo <= i1.hi:
            return True
        return False
          
    def overlabSearch(self,node,i):
        if node == None : return None
        
        if self.doOverlab(node.i,i):
            return node.i
        if node.left != None and node.left.maxi >= i.lo:
            return self.overlabSearch(node.left,i)
        return self.overlabSearch(node.right,i)
        
        
    
    def inorder(self,node):
        if node == None: return
        
        self.inorder(node.left)
            
        print(node.i.lo,node.i.hi,node.maxi)
        
        self.inorder(node.right)
        
    def deletion(self,node):
        if node is None: return
        
            
        
        
        
        
tree = ITree()

node1 = ITNode(Interval(1,4))
node2 = ITNode(Interval(1,5))
node3 = ITNode(Interval(1,6))
node4 = ITNode(Interval(1,7))
node5 = ITNode(Interval(2,5))
node6 = ITNode(Interval(3,5))

tree.insertion(node1)
tree.insertion(node2)
tree.insertion(node3)
tree.insertion(node4)
tree.insertion(node5)
tree.insertion(node6)

tree.inorder(tree.head)

x = Interval(1,7)

a = tree.overlabSearch(tree.head,x)
print(a)


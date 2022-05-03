import sys
import collections

Interval = collections.namedtuple('Interval',['lo','hi'])

class ITNode(object):
    def __init__(self,Interval):
        self.i = Interval
        self.maxi = Interval.hi
        self.left = None
        self.right = None
        self.parent = None
        
    
    def __str__(self):
        return '{}'.format(self.i)
    def __del__(self):
        return
        
overlab = []       
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
                node.parent = head
            else:
                if head.left.maxi < node.i.hi:
                    head.left.maxi = node.i.hi
                self.__insertion(head.left,node)
        else:
            if head.right == None:
                head.right = node
                node.parent = head
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
          
#    def overlabSearch(self,node,i):
#        if node == None : return None
#        
#        if self.doOverlab(node.i,i):
#            overlab.append(node.i)
#            self.overlabSearch(node.left,i)
#            self.overlabSearch(node.right,i)
#            return 
#        if node.left != None and node.left.maxi >= i.lo:
#            return self.overlabSearch(node.left,i)
#        return self.overlabSearch(node.right,i)

    
    
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
        if node == None : return
        
        if node.left == None:
            if node.right == None:
                del node
                return
            tmp = node.right
            tp = node.parent
            del node
            if tp == None:
                return           
            if tp.right == None:
                tp.right = tmp
            else:
                tp.left = tmp
        
        nnext = node.left
        if nnext.right != None :
            while nnext.right != None:
                nnext = nnext.right
                
        node.maxi = max(node.left.maxi,node.right.maxi)
        node.i = nnext.i
        nnext.parent.right = nnext.left
        del nnext
        
        
              
        
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


#for i in range(6):
#    l,h = map(int,input().split())
#    node = ITNode(Interval(l,h))
#    tree.insertion(node)

print(node2.parent)

tree.inorder(tree.head)

tree.deletion(tree.head)
print('----------------')
tree.inorder(tree.head)
print(tree.head)

x = Interval(1,7)

a = tree.overlabSearch(tree.head,x)
print(a)
print(overlab)
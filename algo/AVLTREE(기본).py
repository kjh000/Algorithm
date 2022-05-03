# -*- coding: utf-8 -*-
"""
AVL Tree
"""
class NodeAVL(object):
    def __init__(self,value = None,height = 1):
        self.value = value
        self. height = height
        self.left = None
        self.right = None
        
        
    def _is_leaf(self):
        return not self.right and not self.left
    
    def _get_max_height(self):
        heightr , heightl = 0,0
        if self.right:
            heightr = self.right._get_max_height()+1
        if self.left:
            heightl = self.left._get_max_height()+1
            
        return max(heightl,heightr)
    
    def get_height(self,node):
        if not node:
            return 0
        return node.height
    
    def get_balance(self):
        return self.get_height(self.left) - self.get_height(self.right)
    
    def get_min_value_node(self,node):
        if node is None or node.left is None:
            return node
        return self.get_min_value_node(node.le)
    
    def insert(self,value):
        new_node = NodeAVL(value)
        if value < self.value:
            self.left = self.left and self.left.insert(value) or new_node
        elif value > self.value:
            self.right = self.right and self.right.insert(value) or new_node
        else:
            print('중복노드 허용 안함')
        
        return self.rotate(value)
    
    def rotate(self,value):
        self.height = 1 + max(self.get_height(self.left),self.get_height(self.right))
        
        balance = self.get_balance()
        
        if balance > 1:
            if value < self.left.value:
                return self.right_rotate()
            elif value > self.left.value:
                self.left = self.left.left_rotate()
                return self.right_rotate() 
        elif balance < -1:
              if value > self.right.value:
                  return self.left_rotate()
              elif value < self.right.value:
                  self.right = self.right.right_rotate()
                  return self.left_rotate()     
        return self
    
    def left_rotate(self):
        x = self.right
        T2 = x.left
        x.left = self
        self.right = T2
        
        self.height = 1+max(self.get_height(self.left),self.get_height(self.right))
        x.height = 1 + max(self.get_height(x.left),self.get_height(x.right))
        
        return x
    
    def right_rotate(self):
        y = self.left
        T2 = y.right
        y.right = self
        self.left = T2
        
        self.height = 1+max(self.get_height(self.left),self.get_height(self.right))
        y.height = 1 + max(self.get_height(y.left),self.get_height(y.right))
        
        return y
    
    def delete(self,value):
        if value < self.value:
            self.left = self.left and self.left.delete(value)
        elif value > self.value:
            self.right = self.right and self.right.delete(value)
        else:
            if self.left is None:
                tmp = self.right
                self = None
                return tmp
            elif self.right is None:
                tmp = self.left
                self = None
                return tmp
            tmp = self.get_min_value_node(self.right)
            self.value = tmp.value
            self.right = self.right and self.right.delete(tmp,value)
            
        if self is None:
            return None
        return self.rotate(value)
    
class AVLTree(object):
    def __init__(self):
        self.root = None
        
    def is_leaf(self,value):
        node = self.root._search_node_preorder(value)
        if node:
            return node._is_leaf()
        else:
            return False
    def get_node_level(self,value):
        node = self.root._search_node_preorder(value)
        if node:
            return node.level
        else:
            return False
    def is_root(self,value):
        return self.root.value == value
    
    def get_height(self):
        return self.root._get_max_height()
    
    def insert(self,value):
        if not self.root:
            self.root = NodeAVL(value)
        else:
            self.root = self.root.insert(value)
    def delete(self,value):
        self.root = self.root.delete(value)
        
def preorder(root):
    if root:
        print('({0}, {1})'.format(root.value,root.height-1),end='')
        if root.left:
            preorder(root.left)
        if root.right:
            preorder(root.right)
                
myTree = AVLTree()

for i in range(10,100,10):
    myTree.insert(i)
    
preorder(myTree.root)
            
                
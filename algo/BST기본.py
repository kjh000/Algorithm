# -*- coding: utf-8 -*-
"""
binary search tree
"""

class NodeBST(object):
    def __init__(self,value = None, level = 1):
        self.value = value
        self.level = level
        self.left = None
        self.right = None
        
    def __repr__(self):
        return '{}'.format(self.value)
    
    def _add_next_node(self,value,level_here = 2):
        
        new_node = NodeBST(value,level_here)
        if value > self.value:
            self.right = self.right and self.right._add_next_node(value,level_here+1) or new_node
        elif value < self.value:
            self.left = self.left and self.left._add_next_node(value,level_here+1) or new_node
        else:
            #print('중복노드 허용 안함')
            aa = None
        return self
        
    def _is_leaf(self):
        return not self.right and not self.left
    
    def _get_max_height(self):
        heightr , heightl = 0,0
        if self.right:
            heightr = self.right._get_max_height()+1
        if self.left:
            heightl = self.left._get_max_height()+1
            
        return max(heightl,heightr)
    
    def _search_node(self,value):
        if self.value == value:
            return self
        elif self.left and value < self.value:
            return self.left._search_node(value)
        elif self.right and value > self.value:
            return self.right._search_node(value)
        else:
            return False
        
        
class BinarySearchTree(object):
    def __init__(self):
        self.root = None
    
    def add_node(self,value):
        if not self.root:
            self.root = NodeBST(value)
        else:
            self.root._add_next_node(value)
            
        
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
    
    
    

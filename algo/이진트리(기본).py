# -*- coding: utf-8 -*-
"""
binary tree by node
"""
        
class NodeBT(object):
    def __init__(self,value=None,level = 1):
        self.value = value
        self.level = level
        self.left = None
        self.right = None
        
    def __repr__(self):
        return '{}'.format(self.value)
    
    def _add_next_node(self,value,level_here = 2):
        new_node = NodeBT(value,level_here)
        if not self.value:
            self.value = new_node
        elif not self.left:
            self.left = new_node
        elif not self.right:
            self.right = new_node
        else:
            self.left = self.left._add_next_node(value,level_here+1)
            
    def _search_node_preorder(self,value):
        if self.value == value:
            return self
        else:
            found = None
            if self.left:
                found = self.left._search_node_preorder(value)
            if self.right:
                found = found or self.right._search_node_preorder(value)
                
        return found
    
    def _is_leaf(self):
        return not self.right and not self.left
    
    def _get_max_height(self):
        heightr , heightl = 0,0
        if self.right:
            heightr = self.right._get_max_height()+1
        if self.left:
            heightl = self.left._get_max_height()+1
            
        return max(heightl,heightr)
    
class BianaryTree(object):
    def __init__(self):
        self.root = None
        
    def add_node(self,value):
        if not self.root:
            self.root = NodeBT(value)
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
    
    
    
    
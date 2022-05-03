# -*- coding: utf-8 -*-
"""
ALPHABETS : CAPITAL
Numbers : 0 ~ 25
"""

ALPHABETS = 26

def toNumber(ch):
    return ord(ch) - 65

class Node(object):
    def __init__(self,key,data = None):
        self.key = key
        self.data = data
        self.children = {}
        
class Trie(object):
    def __init__(self):
        self.head = Node(None)
        
    def insert(self,string):
        cur_node = self.head
        for char in string:
            if char not in cur_node.children:
                cur_node.children[char] = Node(char)
                
            cur_node = cur_node.children[char]
            
        cur_node.data = string
        
    def search(self,string):
        cur_node = self.head
        for char in string:
            if char in cur_node.children:
                cur_node = cur_node.children[char]
            else:
                return False
            
        if cur_node.data != None:
            return True
        
    def starts_with(self,prefix):
        cur_node = self.head
        result = []
        subtrie = None
        
        for char in prefix:
            if char in cur_node.children:
                cur_node = cur_node.children[char]
                subtrie = cur_node
            else:
                return None
            
        queue = list(subtrie.children.values())
        while queue:
            cur = queue.pop()
            if cur.data != None:
                result.append(cur.data)
            queue += list(cur.children.values())
            
        return result
    
    

t = Trie()
#words = ["romane", "romanus", "romulus", "ruben", 'rubens', 'ruber', 'rubicon', 'ruler']
#for word in words:
#    t.insert(word)
#
#print(t.search("romulus"))
#print(t.search("ruler"))
#print(t.search("rulere"))
#print(t.search("romunus"))
#print(t.starts_with("ro"))
#print(t.starts_with("rube"))
#
#print(t.starts_with("aaa"))

#nums = ['911','97625999','91125426']
nums = ['113','12340','123440','12345','98346']
for i in nums:
    t.insert(i)
    
for i in nums:
    a = t.starts_with(i)
    print(a)

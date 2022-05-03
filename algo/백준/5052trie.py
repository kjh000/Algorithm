import sys

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
    
    

T = int(input())

for t in range(T):    
        
    tree = Trie()
    
    
    n = int(input())
    call = []
    
    flag = 0
    
    for i in range(n):
        s = input()
        s = ''.join(s.split())
        call.append(s)
        
    for i in call:
        tree.insert(i)
        
    for i in call:
        
        aa = tree.starts_with(i) 
        if len(aa) == 0:
            pass
        else:
            flag = 1
            break
        
    if flag == 0:
        print('YES')
    else:
        print('NO')
        
    
    del(tree)
    


class node:
    def __init__(self, low, high):
        self.left = None
        self.right = None
        self.highest = high
        self.low = low
        self.high = high

class interval:
    def __init__(self):
        self.head = None
        self.count = 0

    def add_node(self, node):
        if self.head == None:
            self.head = node
        else:
            if self.head.highest < node.high:
                self.head.highest = node.high         
            self.__add_node(self.head, node)

    def __add_node(self, head, node):                   
        if node.low <= head.low:         
            if head.left == None:            
                head.left = node
            else:            
                if head.left.highest < node.high:
                    head.left.highest = node.high
                self.__add_node(head.left, node)
        else:           
            if head.right == None:                
                head.right = node
            else:               
                if head.right.highest < node.high:
                    head.right.highest = node.high          
                self.__add_node(head.right, node)

    def search(self, node):
        self.count = 0
        return self._search(self.head, node)

    def _search(self, head, node):
        if node.low <= head.high and node.high >= head.low:
            self.count += 1 
#        print(self.count, head.high, head.low)        
        if head.left != None and head.left.highest >= node.low:
                return self._search(head.left, node)
        elif head.right != None:
                return self._search(head.right, node)       
        return self.count

n,m = map(int,input().split())

intervals = interval()
for i in range(n):
    a,b = map(int,input().split())
    p = node(a, b)
    intervals.add_node(p)
count = 0
for i in range(m):  
    c,d = map(int,input().split())
    count += intervals.search(node(c, d)) 
print(count)
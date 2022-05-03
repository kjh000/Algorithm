'''
stack by list
'''

class Stack(object):
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return not bool(self.items)
    
    def push(self,value):
        self.items.append(value)
        
    def pop(self):
        value = self.items.pop()
        if value is not None:
            return value
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print('Stack is empty')
    
    def __repr__(self):
        return repr(self.items)
    
stack = Stack()

for i in range(5):
    stack.push(i)
    

while not stack.isEmpty():
    a = stack.pop()
    print(a)
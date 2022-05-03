


class rb_node(object):
    
    def __init__(self,key):
        self.key = key
        self.red = False
        self.left = None
        self.right = None
        self.parent  = None
        
class rb_tree(object):
    
    def __init__(self,create_node = rb_node):
        
        self.nil = create_node(key = None)
        self.root = self.nil
        self.create_node = create_node
        
        
    def search(self,key,x=None):
        if None == x:
            x = self.root
        while x!= self.nil and key != x.key:
            if key<x.key:
                x = x.left
            else:
                x = x.right
        
        return x
    
    def minimum(self,x = None):
        
        if None ==x:
            x = self.root
        while x.left != self.nil:
            x = x.left
        return x
    
    def maximum(self,x = None):
        
        if None == x:
            x = self.root
        while x.right != self.nil:
            x = x.right
        return x
    
    def insert_key(self,key):
        
        self.insert_node(self.create_node(key=key))
        
    def insert_node(self,z):
        y = self.nil
        x = self.root
        
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else: x = x.right
            
        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
            
        z.left = self.nil
        z.right = self.nil
        z.red = True
        self.insert_fixup(z)
        
             
    def insert_fixup(self, z):
        while z.parent.red:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.red:
                    z.parent.red = False
                    y.red = False
                    z.parent.parent.red = True
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.red = False
                    z.parent.parent.red = True
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.red:
                    z.parent.red = False
                    y.red = False
                    z.parent.parent.red = True
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.red = False
                    z.parent.parent.red = True
                    self.left_rotate(z.parent.parent)
        self.root.red = False

    
    def left_rotate(self, x):
        
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left._p = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y


    def right_rotate(self, y):
        
        x = y.left
        y.left = x.right
        if x.right != self.nil:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == self.nil:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x
    

rbt = rb_tree()

mat = [0]*4

for i in range(4):
    mat[i] = rb_node(i)
    rbt.insert_node(mat[i])
    
for i in mat:
    print(rbt.minimum(i).key)
    
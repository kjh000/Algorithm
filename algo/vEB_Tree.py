import math
import time
class Veb(object):
    def __init__(self,u):
        self._u = 2
        tmp = 2
        while (self._u < u):
            self._u = 2**tmp
            tmp = tmp*2

        self._min = None
        self._max = None
        self._cluster = {}
        self._summary = None

    def high(self,x):
        return int(x // math.sqrt(self._u))

    def low(self,x):
        return int(x % math.sqrt(self._u))

    def index(self,i,j):
        return int(i * math.sqrt(self._u) + j)
    def insert(self,x):
        if self._min == None:
            self._min = x
            self._max = x


        else:
            if x < self._min:
                # swap
                tmp = self._min
                self._min = x
                x = tmp
            if x > self._max:
                self._max = x
            if self._u > 2:
                
                h = self.high(x)
                l = self.low(x)
                if self._summary == None:
                    self._summary = Veb(self.high(self._u))
                if h not in self._cluster:
                    self._cluster[h] = Veb(self.high(self._u))
                    
                if self._cluster[h]._min == None:
                    self._summary.insert(h)

                self._cluster[h].insert(l)


    def is_in(self,x):
        if x == self._min or x == self._max:
            return True
        else:
            if self._u == 2:
                return False
            else:
                h = self.high(x)
                l = self.low(x)
                if h not in self._cluster:
                    return False
                return self._cluster[h].is_in(l)
    def __contains__(self, item):
        return self.is_in(item)

    def successor(self,x):
        if self._u == 2:
            if x==0 and self._max == 1:
                return 1
            else:
                return None
        elif self._min!= None and x < self._min:
            return self._min
        else:
            h = self.high(x)
            l = self.low(x)
            i = self.high(x)
            tmp = self._cluster.get(h,None)
            
            
            if tmp != None and tmp._max != None and l < tmp._max:
                j = self._cluster[h].successor(l)
            else:
                i == None
                if self._summary != None:
                    i = self._summary.successor(h)
                if i == None:
                    return None
                tmp = self._cluster.get(i,None)
                if tmp == None:
                    return None
                j = tmp._min

            if j == None:
                return None
            return self.index(i,j)

    def predecessor(self,x):
        if self._u == 2:
            if x==1 and self._min == 0:
                return 0
            else:
                return None
        elif self._max!= None and x > self._max:
            return self._max
        else:
            h = self.high(x)
            l = self.low(x)
            i = self.high(x)
            j = None

            tmp = self._cluster.get(h,None)
            if tmp != None and tmp._min != None and l > tmp._min:
                
                j = self._cluster[h].predecessor(l)
                    
                return self.index(h,j)
                    
            else:
                
                i = None
                if self._summary != None:
                    i = self._summary.predecessor(h)
                if i == None:
                    if self._min != None and x > self._min:
                        return self._min
                    else:
                        return None
                else:
                    tmp = self._cluster.get(i,None)
                    if tmp == None:
                        return None
                    j = tmp._max
                    if j == None:
                        return None
                    return self.index(i,j)
                    
            
            
            #return self.index(i,j)
                
            
                


##v = Veb(10000000)
##print(v._u)
##v.insert(0)
##v.insert(200)
##v.insert(100)
##v.insert(101)
##print(v.is_in(0))
##print(v.is_in(300))
##print(v.is_in(100))
##print(v.successor(200))
##print(v.successor(190))
##print(v.predecessor(0))

num_set = set()
f = open('input.txt','r')
max_num = -1
for line in f:
    num = int(line)
    if num> max_num:
        max_num = num
    num_set.add(num)
v = Veb(max_num)
num_num = len(num_set)

#--- count time for creating tree
print('VEB tree creating for {} elements with range u 0 - {}'.format(num_num,v._u-1))
start_time = time.time()
for num in num_set:
    v.insert(num)
total_time = float(time.time() - start_time)
print('VEB tree created')
print("Insert time amortized: %f seconds" % (total_time / num_num))

#--- count time for successor query
start_time = time.time()
for num in num_set:
    a=v.successor(num)
total_time = float(time.time() - start_time)
print("Successor query time amortized: %f seconds" % (total_time / num_num))

#--- count time for predecessor query
start_time = time.time()
for num in num_set:
    a=v.predecessor(num)
total_time = float(time.time() - start_time)
print("Predecessor query time amortized: %f seconds" % (total_time / num_num))

#--- count time for is_in check
start_time = time.time()
for num in num_set:
    a=v.is_in(num)
total_time = float(time.time() - start_time)
print("Is_in query time amortized: %f seconds" % (total_time / num_num))
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 15:50:19 2019

@author: kjh1
"""

import queue
import threading
import time

##########FIFO
q = queue.Queue()

q.put(5)

print(q.get())

print(q.empty())


for i in range(5):
    q.put(i)
    
while not q.empty():
    print(q.get(), end = '  ')

########### out put 5,True , 0 1 2 3 4 

q = queue.Queue()

q.put(5)

print(q.get())
print('first item gotten')

print(q.get())
print('finished')
#
############# error code freeze console
    
############# following code is correct
#
#def putting_thread(q):
#    while True:
#        print('starting thread')
#        time.sleep(10)
#        q.put(5)
#        print('put something')
#        
#        
#q = queue.Queue()
#
#t= threading.Thread(target = putting_thread, args = (q,), daemon=True)
#t.start()
#q.put(5)
#
#print(q.get())
#print('first item gotten')
#
#print(q.get())
#print('finished')

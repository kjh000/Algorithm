# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 16:08:00 2019

@author: kjh1
"""

import queue

############# FIFO 
q = queue.Queue()
#
#for i in range(5):
#    q.put(i)
#    
#while not q.empty():
#    print(q.get(), end = '')
#    
#    
#print('\n')
#
#
################ LIFO
#q2 = queue.LifoQueue()
#
#for i in range(5):
#    q2.put(i)
#    
#while not q2.empty():
#    print(q2.get(),end = '')
#    
#    
#    
#print('\n')
#
###################Priority 
#
#q3 = queue.PriorityQueue()
#q3.put((1, 'priority 1'))
#q3.put((3, 'priority 3'))
#q3.put((4, 'priority 4'))
#q3.put((2, 'priority 2'))
#
#
#for i in range(q3.qsize()):
#    print(q3.get()[1])

q.put(1)

c = q.get_nowait()

print(c)

c = q.get_nowait()
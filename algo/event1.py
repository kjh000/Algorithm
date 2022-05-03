# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 09:49:05 2019

@author: kjh1
"""

import threading
import time
import queue
import numpy as np

#event = threading.event()

#event.set() -> set true(green flag)
#event.clear() -> red flag
#event.wait() - blocking progress untill set()




def flag():
    time.sleep(3)
    event.set()
    print('starting countdown \n')
    time.sleep(7)
    print('event is cleared')
    event.clear()
    
    
    
def start_operations():
    event.wait()
    while event.is_set():
        print('starting random inteager task')
        x = np.random.randint(1,30)
        time.sleep(.5)
        if x == 29:
            print('True')

    print('Event has been cleared, random operation stops')
        
    
event = threading.Event()

t1 = threading.Thread(target=flag)
t2 = threading.Thread(target=start_operations)

t1.start()
t2.start()


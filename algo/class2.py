# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 18:40:49 2019

@author: kjh1
"""

def __init__(self,group=None, target=None, name= None,
             args=(), kwargs=None, *, daemon=None):
    
    
    
import threading
import time



        

class MyThread(threading.Thread):
    
    def run(self):
        print('{} has started!'.format(self.getName()))
        try:
            if self._target:
                self._target(*self._args,**self._kwargs)
    
        finally:
            del self._target, self._args, self._kwargs
        
        print('{} has finished!'.format(self.getName()))
        

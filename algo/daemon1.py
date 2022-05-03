# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 15:07:28 2019

@author: kjh1
"""

import threading
import time



total = 4

def creates_items():
	global total
	for i in range(10):
		time.sleep(2)
		print('added item')
		total += 1
	print('creation in done')
	
	
def creates_items_2():
	global total
	for i in range(7):
		time.sleep(10)
		print('added item')
		total += 1
	print('creation is done')
	
	
def limits_items():

	global total
	while True:
		if total >5:
		
			print('overload')
			total -= 3
			print('subtracted 3')
		else:
			time.sleep(1)
			print('waiting')
			
			
creater1 = threading.Thread(target = creates_items)
creater2 = threading.Thread(target = creates_items_2)
limitor = threading.Thread(target = limits_items, daemon = True)

print(limitor.isDaemon())

creater1.start()
creater2.start()
limitor.start()

creater1.join()
creater2.join()





print(' our ending value of total is ', total)



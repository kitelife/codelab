#-*- coding: utf-8 -*-

#subtly bad design because of shared staet

import threading
import time

count = 1

class kissThread(threading.Thread):
	def run(self):
		global count  #这里通过global声明count为全局变量
		print 'Thread # %s:Pretending to do stuff' %count
		count += 1
		time.sleep(2)
		print 'done with stuff'

for t in range(5):
	print t
	kissThread().start()

#-*- coding: utf-8 -*-
from processing import Process, Queue
import time

def f(q):
	x = q.get()
	print 'Process Number %s, sleeps for %s seconds'%(x, x)
	time.sleep(x)
	print 'Process Number %s finished' %x

q = Queue()

for i in range(10):
	q.put(i)
	p = Process(target=f, args = [q])
	p.start()

print 'main process joins on queue'
p.join()
'''
为什么
main process joins on queue
出现的位置不固定，
难道是因为给进程分配资源需要时间而导致的么？？？
'''
print 'main process finished'

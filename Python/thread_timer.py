#-*- coding : utf-8 -*-

from threading import Timer
import sys
import time
import copy

#simple error handling
if len(sys.argv)!=2:
	print 'Must enter an interval'
	sys.exit(1)

#out function that we will run
def hello():
	print 'Hello, I just got called after a %s sec delay' %call_time #靠，这样使用call_time也行啊？！

#we spawn our time delayed thread here
delay = sys.argv[1]
call_time = copy.copy(delay) #we copy the delay to use later
t = Timer(int(delay),hello)
t.start()

#we valiate that we are not blocked, and that the main program continues
print 'waiting %s seconds to run function' % delay

for x in range(int(delay)):
	print 'Main program is still running for %s more sec'%delay
	delay = int(delay) - 1
	time.sleep(1)

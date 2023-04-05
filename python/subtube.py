#-*- coding: utf-8 -*-

from subprocess import call
import time
import sys

'''
Subtube is module that simplifies and automates some aspects of subprocess
'''

class BaseArgs(object):
	'''
	Base Argument Class that handles keyword argument parsing
	'''

	def __init__(self, *args, **kwargs): #what is **kwargs ???
		self.args = args
		self.kwargs = kwargs #kwargs是反向读入的
		if self.kwargs.has_key('delay'):
			self.delay = self.kwargs['delay']
		else:
			self.delay=0
		if self.kwargs.has_key('verbose'):
			self.verbose = self.kwargs['verbose']
		else:
			self.verbose = False
	
	def run(self):
		'''
		you must implement a run method
		'''
		raise NotImplementedError

class Runner(BaseArgs):
	'''
	Simplifies subprocess call and runs call over a sequence of commands
	Runner takes N positional arguments ,and optionally:

	[optional keyword parameters]
	delay=1, for time delay in seconds
	verbose = True for verbose output

	usage:

	cmd = Runner('ls -l','df -h',verbose = True, delay =3) #由此可看出**kwargs的含义
	cmd.run()
	'''

	def run(self):

		print self.kwargs
		print self.args	
		for cmd in self.args:
			if self.verbose:
				print 'Running %s with delay=%s' %(cmd, self.delay)
			time.sleep(self.delay)
			call(cmd,shell = True)

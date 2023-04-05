#!/usr/bin/python
#wraps up rsync to synchronize two directories

from subprocess import call
import sys
import time

'''This motivated rsync tries to synchronize forever'''

source = '/tmp/sync_dir_A/' #Note the trailing slash
target = '/tmp/sync_dir_B'
rsync = 'rsync'
arguments = '-av'
cmd = '%s %s %s %s' %(rsync, arguments, source, target)

def sync():
	while True:
		ret = call(cmd, shell = True)
		if ret !=0:
			print 'resubmitting rsync!'
			time.sleep(30)
		else :
			print 'rsync was successful'
			subprocess.call('mail -s "jobs done" bofn@example.com',shell = True)
			sys.exit(0)

sync()

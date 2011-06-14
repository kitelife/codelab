#-*- coding: utf-8 -*-
#!/usr/bin/python

#wraps up rsync to synchronize two directories
#<Python for Unix and linx administration>一书示例6-13

from subprocess import call
import sys

source = '/tmp/sync_dir_A/' #Note the trailing slash
target = '/tmp/sync_dir_B'
rsync = 'rsync'
arguments = '-a'

cmd = '%s %s %s %s' % (rsync, arguments, source, target)

def sync():
	ret = call(cmd, shell = True)
	if ret != 0:
		print 'rsync failed'
		sys.exit(1)

sync()

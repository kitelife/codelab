#-*- coding: utf-8 -*-

import _mysql
import sys

try:
	conn = _mysql.connect('localhost', 'testuser',
	'test623', 'testdb')
	
	conn.query('SELECT VERSION()')
	result = conn.use_result()
	
	print "MySQL version: %s" %\
		result.fetch_row()[0]
		
	conn.close()
	
except _mysql.Error, e:
	
	print "Error %d: %s" % (e.args[0], e.args[1])
	sys.exit(1)
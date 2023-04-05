#-*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

try:
	conn = mdb.connect('localhost', 'testuser', 'test623', 'testdb')
	
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM Writes')
	
	rows = cursor.fetchall()
	
	for row in rows:
		print row
		
	cursor.close()
	conn.close()
	
except mdb.Error, e:
	
	print 'Error %d: %s' %(e.args[0], e.args[1])
	sys.exit(1)
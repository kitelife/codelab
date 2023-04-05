#-*- coding: utf-8 -*-
import MySQLdb as mdb
import sys

try:
	conn = mdb.connect('localhost', 'testuser', 'test623', 'testdb')
	
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM Writes')
	
	numrows = int(cursor.rowcount)
	
	for i in range(numrows):
		row = cursor.fetchone()
		print row[0], row[1]
	
	cursor.close()
	conn.close()
	
except mdb.Error, e:
	
	print 'Error %d: %s' %(e.args[0], e.args[1])
	exit(1)
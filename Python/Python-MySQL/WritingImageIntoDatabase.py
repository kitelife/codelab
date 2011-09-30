#-*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

try:
	fin = open("chrome.png")
	img = fin.read()
	fin.close()
	
except IOError, e:
	
	print 'Error %d: %s' %(e.args[0], e.args[1])
	sys.exit(1)
	
try:
	conn = mdb.connect(host = 'localhost', user = 'testuser',
	passwd = 'test623', db = 'testdb')
	
	cursor = conn.cursor()
	cursor.execute("INSERT INTO Images SET Data = '%s'" %
	mdb.escape_string(img))
	
	conn.commit()
	
	cursor.close()
	conn.close()
	
except mdb.Error, e:
	print 'Error %d: %s' %(e.args[0], e.args[1])
	sys.exit(1)
#-*- utf-8 -*-

import MySQLdb as mdb
import sys

try:
	conn = mdb.connect('localhost', 'testuser', 'test623', 'testdb')
	
	cursor = conn.cursor()
	cursor.execute("CREATE TABLE IF NOT EXISTS \
	Writes(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25))")
	cursor.execute("INSERT INTO Writes(Name) VALUES('Jack London')")
	cursor.execute("INSERT INTO Writes(Name) VALUES('Honore de Balzac')")
	cursor.execute("INSERT INTO Writes(Name) VALUES('Lion Feuchtwanger')")
	cursor.execute("INSERT INTO Writes(Name) VALUES('Emile Zola')")
	cursor.execute("INSERT INTO Writes(Name) VALUES('Truman Capote')")
	
	conn.commit()
	
	cursor.close()
	conn.close()
	
except mdb.Error, e:
	
	print 'Error %d: %s' %(e.args[0], e.args[1])
	sys.exit(1)
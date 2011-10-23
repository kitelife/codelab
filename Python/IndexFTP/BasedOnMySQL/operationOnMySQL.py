#!/usr/bin/python

#-*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import operateLog

class MySQLdbOperation():

	def __init__(self, host, userName, passwd, dbName):

		self.host = host
		self.userName = userName
		self.passwd = passwd
		self.dbName = dbName
		try:
			self.conn = mdb.connect(self.host, self.userName, self.passwd, self.dbName)
			#cursor = self.conn.cursor()
		except mdb.Error, e:
			exceptMessage = 'Error %d: %s' %(e.args[0], e.args[1])
			operateLog.writeLog(exceptMessage)
			#print 'Error %d: %s' %(e.args[0], e.args[1])
			sys.exit(1)

	def createTable(self):
		cursor = self.conn.cursor()
		try:
			cursor.execute("CREATE TABLE IF NOT EXISTS filelist( \
				Id INT PRIMARY KEY AUTO_INCREMENT, \
				fileName VARCHAR(200), \
				Path VARCHAR(400), \
				lastTimeModified VARCHAR(25)\
				)")
			self.conn.commit()
		except mdb.Error, e:
			exceptMessage = 'Error %d: %s' %(e.args[0], e.args[1])
			operateLog.writeLog(exceptMessage)
			#print 'Error %d: %s' %(e.args[0], e.args[1])
			cursor.close()
			#self.conn.close()
			#sys.exit(1)

	def queryData(self, SQL):
		cursor = self.conn.cursor()
		try:
			cursor.execute(SQL)
			rows = cursor.fetchall()

			return rows
		except mdb.Error, e:
			exceptMessage = 'Error %d: %s' %(e.args[0], e.args[1])
			operateLog.writeLog(exceptMessage)
			#print 'Error %d: %s' %(e.args[0], e.args[1])
			cursor.close()
			#self.conn.close()

	def addData(self, fileName, Path, lastTimeModified):
		#print fileName
		cursor = self.conn.cursor()
		SQL = 'INSERT INTO filelist (fileName, Path, lastTimeModified) VALUES("%s", "%s", "%s")' %(fileName, Path, lastTimeModified)
		#print SQL
		operateLog.writeLog('Insert %s' %fileName)

		try:
			cursor.execute(SQL)
			self.conn.commit()
		except mdb.Error, e:
			exceptMessage = 'Error %d: %s' %(e.args[0], e.args[1])
			operateLog.writeLog(exceptMessage)
			#print 'Error %d: %s' %(e.args[0], e.args[1])
			cursor.close()
			return -1
		return 0

	def dropTable(self, tableName):
		cursor = self.conn.cursor()
		sqlSentence = 'DROP TABLE %s' %tableName
		try:
			cursor.execute(sqlSentence)
		except mdb.Error, e:
			exceptMessage = 'Error %d: %s' %(e.args[0], e.args[1])
			operateLog.writeLog(exceptMessage)
			cursor.close()
			return -1
		return 0

	def closeLink(self):
		self.conn.close()

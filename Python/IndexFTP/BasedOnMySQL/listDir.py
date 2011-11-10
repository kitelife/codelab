#!/usr/bin/python

#-*- coding: utf-8 -*-

import sys
import os
import time

import operationOnMySQL
import operateLog
#-----------------------------------
host = 'xxx'
userName = 'xxx'
passwd = 'xxx'
dbName = 'xxx'
#-----------------------------------

def listFileInThisDir(directory):

	operateMySQL = operationOnMySQL.MySQLdbOperation(host, userName, passwd,dbName)
	operateMySQL.dropTable('filelist')
	operateMySQL.createTable()

	#fileHandler = open('fileList.txt','w')
	for root, dirs, files in os.walk(directory):
		for fi in files:
			filePath = root + '/' + fi
			filePath = filePath.replace('//','/')
			fileInfo = os.stat(filePath)
			if "/var/ftp/project" in filePath:
				filePath = filePath.replace("/var/ftp/project","ftp://202.120.40.124:2121")
			else:
				filePath = filePath.replace("/var/ftp","ftp://202.120.40.124:2121")
			timeInlist = list(time.localtime(fileInfo.st_ctime)[:6])
			lenOfTimeList = len(timeInlist)
			for index in range(lenOfTimeList):
				timeInlist[index] = str(timeInlist[index])
			fileTime = '-'.join(timeInlist)
			#dataFromQuery = operateMySQL.queryData('SELECT * FROM filelist WHERE Path = "%s"' %filePath)
			#if dataFromQuery != None:
			#	lenOfRows = len(dataFromQuery)

			#fileHandler.write(fi+'  '+filePath+'  '+fileTime+'\n')
			#if dataFromQuery == None or lenOfRows == 0:
			print "add one file"
			operateMySQL.addData(fi, filePath, fileTime)

	#for row in operateMySQL.queryData("SELECT * FROM filelist"):
	#	print row[0], row[1], row[2], row[3]

	operateMySQL.closeLink()

if __name__ == '__main__':
	logger = operateLog.initLog()
	
	#beginMessage = '***** Begin list FTP directory at : ' + time.ctime() + ' *****\n'
	#operateLog.writeLog(beginMessage)
	
	beginMessage = 'Begin list FTP directory.'
	logger.info(beginMessage)

	listFileInThisDir('/var/ftp/project/+WSN/')
	
	#endMessage = '##### End list FTP directory at: ' + time.ctime() + ' #####\n'
	#operateLog.writeLog(endMessage)
	endMessage = 'End list FTP directory'
	logger.info(endmessage)

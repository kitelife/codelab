#!/usr/bin/python

#-*- coding: utf-8 -*-
logs = 'LogForListFTP.txt'

def writeLog(message):
	logFile = open(logs, 'a')
	logFile.write(message + '\n')
	logFile.close()

loggingFile = 'indexFtp.log'

def initLog():
	import logging

	logger = logging.getLogger()
	hdlr = logging.FileHandler(loggingFile)
	formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
	hdlr.setFormatter(formatter)
	logger.addHandler(hdlr)
	logger.setLevel(logging.NOTSET)

	return logger

#!/usr/bin/python

#-*- coding: utf-8 -*-
logs = 'LogForListFTP.txt'

def writeLog(message):
	logFile = open(logs, 'a')
	logFile.write(message + '\n')
	logFile.close()

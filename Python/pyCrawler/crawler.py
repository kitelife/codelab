#-*- coding:utf-8 -*-
import urllib2
import sys
#import time
import os

from HTMLParser import HTMLParser
import chardet

def changeCoding(string):
	detResult=chardet.detect(string)
	coding=detResult['encoding']
	#print coding
	string=unicode(string,coding).encode('gb2312')
	return string

dirName = 'D:/Test/'
typeList = ['html','jpg','jpeg','pdf','doc','gif','ppt','xls','pptx','docx','pptx','rar','zip']

def getPage(address):
	tomkdir = address.split('://')[1]
	partialPath = tomkdir.split('/')
	print partialPath
	tempPath = dirName
	if partialPath[-1] == '':
		partialPath.pop()
	if len(partialPath)>1:
		for index in range(len(partialPath)-1):
			tempPath = tempPath + '/' + partialPath[index]
			tempPath = changeCoding(tempPath)
			if not os.path.exists(tempPath):
				os.mkdir(tempPath)
	filename = changeCoding(partialPath[-1])
	print filename
	filename = tempPath+'/'+filename
	content = None

	try:
		content = urllib2.urlopen(address).read()
	except :
		pass
	if content != None:

		filetype = filename.split('.')[-1]
		if not (filetype in typeList):
			filename = filename + '.html'
		pagefile = open(filename,'w')
		pagefile.write(content)
		pagefile.close()
		return content

linksList=list()
getedLinksList=list()

class MyHTMLParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
	def handle_starttag(self, tag, attrs):
		#print "Encountered the beginning of a %s tag" % tag
		if tag == "a":
			if len(attrs) == 0:
				pass
			else:
				for (variable, value)  in attrs:
					if (variable == "href") and (value.startswith('http')) and\
					 (not (value in getedLinksList)) and (not (value in linksList)):
						linksList.append(value)
 
if __name__ == "__main__":
	linksList.append(sys.argv[1])
	maxN = 0
	while(len(linksList)>0 and maxN < 100):
		address=linksList[-1]
		print address
		getedLinksList.append(linksList.pop())
		hpn = MyHTMLParser()
		try:
			hpn.feed(getPage(address))
			hpn.close()
		except:
			pass
		maxN = maxN + 1

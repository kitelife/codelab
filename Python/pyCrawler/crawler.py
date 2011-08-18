#-*- coding:utf-8 -*-

import urllib2
import sys
import os

from HTMLParser import HTMLParser
import chardet

def changeCoding(string):
	detResult=chardet.detect(string)
	coding=detResult['encoding']
	#print coding
	string=unicode(string,coding).encode(sys.stdin.encoding)
	return string

dirName = 'D:/Test/'
typeList = {'htm':0,'html':0,'mp3':0,'jpg':0,'jpeg':0,'pdf':0,'doc':0,'gif':0,'ppt':0,
	    'xls':0,'pptx':0,'docx':0,'pptx':0,'rar':0,'zip':0,'php':0,'css':0,'js':0,
	    'png':0,'asp':0,'aspx':0,'jsp':0,'rss':0,'xml':0}

def getPage(address):
	tomkdir = address.split('://')[1] #去除URL的头部"http://"
	partialPath = tomkdir.split('/')  #根据URL的路径层次生成层次化目录，用于存储爬取的网页文件
	#print partialPath
	tempPath = dirName
	if partialPath[-1] == '':
		partialPath.pop()
	if len(partialPath)>1:
		for index in range(len(partialPath)-1):
			tempPath = tempPath + '/'+ partialPath[index]
			tempPath = changeCoding(tempPath)

	filename = changeCoding(partialPath[-1])
	print filename
	filename = tempPath+'/'+filename
	content = None

	try:
		content = urllib2.urlopen(address).read()
	except :
		pass
	if content != None:
		if not os.path.exists(tempPath):
			os.mkdir(tempPath)

		filetype = filename.split('.')[-1]
		if (filetype in typeList.keys()):
			typeList[filetype] += 1
		#if not (filetype in typeList): #如果URL是动态生成的，也就是没有明确的文件后缀名表示的文件类型，则不管是什么东西都把当作html文件
		else:
			filename = filename + '.html'
			typeList['html'] += 1
		pagefile = open(filename,'w')
		pagefile.write(content)
		pagefile.close()
		return content
	
linksList = list()
getedLinksList = list()

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
	while(len(linksList)>0 and maxN < 1000):
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

	#按值对字典内容进行排序,生成一个元组的列表
	anotherTypeList = sorted(typeList.iteritems(), key = lambda d:d[1], reverse = True)

	numOfFiles = 0
	for value in typeList.values():
		numOfFiles += value
	statistics = ''
	for item  in anotherTypeList:
		numOfThisFile = float(item[1])
		statistics = statistics + item[0] +' ---> '+ str(numOfThisFile) + ' ---> ' + str(numOfThisFile/numOfFiles) + '\n'
	print statistics
	statisticsFile = open(dirName+'statistics.txt','w')
	statisticsFile.write(statistics)
	statisticsFile.close()
	
	links = ''
	for link in getedLinksList:
		links = links + link + '\n'
	fileForLink = open(dirName+'getedLinks.txt','w')
	fileForLink.write(links)
	fileForLink.close()

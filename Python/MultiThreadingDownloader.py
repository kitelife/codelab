#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import time
import urllib

from threading import Thread

exampleProxy = {'http':'http://localhost:8080/'} #还不明白这个的作用

class multiThreadDownload(Thread,urllib.FancyURLopener):
    def __init__(self, threadname, url, filename, ranges=0,proxies={}):
		Thread.__init__(self, name=threadname)
		urllib.FancyURLopener.__init__(self,proxies)
		self.name = threadname
		self.url = url
		self.filename = filename
		self.ranges = ranges
		self.downloaded = 0
	def run(self):
		'''Virtual method in Thread'''
		try:
			self.downloaded = os.path.getsize( self.filename )
		except OSError:
			#print 'never downloaded'
			self.downloaded = 0

		# rebuild start poind
		self.startpoint = self.ranges[0] + self.downloaded
		if self.startpoint >= self.ranges[1]:
			print 'Part %s has been downloaded over.' % self.filename
			return
       
		self.oneTimeSize = 16384 #16kByte/time
		print 'task %s will download from %d to %d' % (self.name, self.startpoint, self.ranges[1])
		
		self.addheader("Range", "bytes=%d-%d" % (self.startpoint, self.ranges[1]))   #.....................   
		
		self.urlhandle = self.open( self.url )
		
		data = self.urlhandle.read( self.oneTimeSize )
		
		while data:
			filehandle = open( self.filename, 'ab+' )
			filehandle.write( data )
			filehandle.close()
			
			self.downloaded += len( data )
			data = self.urlhandle.read( self.oneTimeSize )

'''
def getURLFileSize(url):
	file = urllib2.urlopen(url)
	fileContent = file.read()
	length = len(fileContent)
	print length
	return length
'''
'''
开始我尝试用上面这个方法来获取需要下载的文件的大小，但发现很慢，究其原因是---上面
获取文件大小的方法是先获得文件的内容，然后根据内容计算出文件的大小，这就意味着在
计算大小之前需要直接下载文件，当然非常的慢...而且这样的话后面的多线程就多此一举了...
'''
def getURLFileSize(url,proxies={}):
	urlHandler = urllib.urlopen(url,proxies=proxies)
	headers = urlHandler.info().headers
	length = 0
	for header in headers:
		if header.find('Length')!=-1:
			length = header.split(':')[-1].strip()
			length = int(length)
	return length
def SpliteBlocks(totalsize, blocknumber):
    blocksize = totalsize/blocknumber
    ranges = []
    for i in range(0, blocknumber-1):
        ranges.append((i*blocksize, i*blocksize +blocksize - 1))
    ranges.append(( blocksize*(blocknumber-1), totalsize -1 ))

    return ranges
def islive(tasks):
    for task in tasks:
        if task.isAlive():
            return True
    return False

def paxel(url, output, blocks=6,proxies=exampleProxy):
    ''' paxel
    '''
    size = getURLFileSize(url,proxies)
    ranges = SpliteBlocks( size, blocks )

    threadname = [ "thread_%d" %i for i in range(0, blocks) ]
    filename = [ "tmpfile_%d" %i for i in range(0, blocks) ]
 
    tasks = []
    for i in range(0,blocks):
        task = multiThreadDownload( threadname[i], url, filename[i], ranges[i],)         #???
        task.setDaemon( True )
        task.start()
        tasks.append( task )
       
    time.sleep( 2 )
    while islive(tasks):
		downloaded = sum( [task.downloaded for task in tasks] )
		process = downloaded/float(size)*100
		show = u'\rFilesize:%d Downloaded:%d Completed:%.2f%%' % (size, downloaded, process)	
		sys.stdout.write(show)
		sys.stdout.flush()
		time.sleep( 0.5 )
           
    filehandle = open( output, 'wb+' )
    for i in filename:
        f = open( i, 'rb' )
        filehandle.write( f.read() )
        f.close()
        try:
            os.remove(i)
            pass
        except:
            pass

    filehandle.close()

if __name__ == '__main__':
    '''
使用方法：python pyDownloader.py 线程数目  文件的URL
    '''
	url = sys.argv[2]
	output = url.split('/')[-1]
	paxel( url, output, blocks=int(sys.argv[1]),proxies={})
	print '\n'
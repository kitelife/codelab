#-*- coding: utf-8 -*-

import chardet #第三方库，下载地址：http://chardet.feedparser.org/download/
import sys
import os

def changeCoding(path):
	for root,dirs,files in os.walk(path):
		for file in files:
			if file.endswith('.java'): #这里只对java文件进行转换编码，去掉这一行就可以对所有的文件对转换编码为utf-8
				filepath=root+'/'+file
				print filepath
				fp=open(filepath)
				content=fp.read()
				fp.close()
				detResult=chardet.detect(content)
				coding=detResult['encoding']
				print coding
				if coding == 'GB2312':
					content=unicode(content,coding).encode('utf-8')
					fp=open(filepath,'w')
					fp.write(content)
					fp.close()

if __name__ == '__main__':
	'''
	windows系统的默认编码是gbk/GB2312,而linux系统默认编码是utf-8，所以很多时候从windows系统中拷贝过来的文件
	在linux上会出现中文乱码，特别是对于程序员来说，各种语言源代码等，手动修改很麻烦。所以我就写了这个
	程序用于转换java程序文件的编码
	'''
	changeCoding(sys.argv[1])

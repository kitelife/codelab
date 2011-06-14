#-*- coding: utf-8 -*-

import os
import sys

def modifyName(name):
	if 'u1conflict'in name:
		fileNameParts=name.split('.u1conflict')
		for part in fileNameParts:
				print part
		print '*'*80
		filepathO=root+'/'+name
		filepathN=root+'/'+fileNameParts[0]
		os.rename(filepathO,filepathN)

if __name__ == "__main__":
	'''装了软件Ubuntu One之后，它把一些同步的文件夹名，文件名加上了后缀'.u1conflict'，
	后来那些文件夹我又不想同步了。想把名字都改回来，但需要修改的文件夹文件太多，就只好写了
	这个程序用于自动修改
	'''
	for root,dirs,files in os.walk(sys.argv[1]):
		for file in files:
			modifyName(file)
		for directory in dirs:
			modifyName(directory)

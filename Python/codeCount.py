#-*- coding: utf-8 -*-

import os

linecount = 0 
filecount = 0
commentcount = 0
blanklinecount=0

for root,dirs,files in os.walk('/home/xyf/workspace/AndroidContacts/src':
	for fileName in os.listdir(root):
		if fileName.endswith('.java'):
			filepath=root+'/'+fileName
			print filepath
			filecount+=1
			fileHandler=open(filepath)
			content=fileHandler.readline()
			for line in content:
				line=line.lstrip()
				line=line.rstrip()
				if line.startswith('/'):
					commentcount+=1
				elif line=='':
					blanklinecount+=1	
				else:
					linecount+=1

print filecount
print linecount
print commentcount
print blanklinecount

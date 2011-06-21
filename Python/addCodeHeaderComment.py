############################################################
# Date:2011 06 21
#
# Author:youngsterxyf
#
# FuncDescription: 'This code is for adding HeaderComment to some code file'
#
############################################################

import sys,os
import datetime

def addHeaderComment(codeFileName,funcDescription):
	if '/' not in codeFileName:
		codeFileName = os.getcwd()+'/'+codeFileName
	
	fileHandle=open(codeFileName)
	content = fileHandle.read()
	fileHandle.close()

	now = datetime.datetime.today()
	date = now.strftime('%Y %m %d')
	date = '# Date:'+date+'\n#\n'
	author = '# Author:youngsterxyf\n#\n'
	funcDescription= '# FuncDescription:'+funcDescription+'\n#\n'
	headerComment='#'*60+'\n'+date+author+funcDescription+'#'*60+'\n\n'

	content=headerComment+content

	fileHandle = open(codeFileName,'w')
	fileHandle.write(content)
	fileHandle.close()

if __name__ == '__main__':
	argNumber = len(sys.argv)
	if argNumber == 1:
		print 'Please give me a file'
	elif argNumber == 2:
		addHeaderComment(sys.argv[1],'')
	else:
		funcDescription = ''
		for i in range(2,len(sys.argv)):
			funcDescription = funcDescription+' '+sys.argv[i]
		addHeaderComment(sys.argv[1],funcDescription)
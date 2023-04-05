import sys
import time

def invertedIndex(filename):

	f=open(filename)
	lines=f.readlines()
	f.close()
	wordDict={}
	starttime=time.time()
	for line in lines:
		line=line.replace('\n','')
		lineList=line.split(' ')
	
		keys=wordDict.keys()
		count=0
		for key in keys:
			if lineList[1]==key:
				count +=1
	#	print count
		if count==0:
			wordDict[lineList[1]]=[lineList[0]]
		else:
			wordDict[lineList[1]].append(lineList[0])
	for key in wordDict.keys():
		valueList=wordDict.get(key)
		length=len(valueList)
		print length,
		for file in valueList:
			print key+' <-> '+file,
		print 
	print time.time()-starttime

if len(sys.argv)<2:
	pass
else:
	invertedIndex(sys.argv[1])

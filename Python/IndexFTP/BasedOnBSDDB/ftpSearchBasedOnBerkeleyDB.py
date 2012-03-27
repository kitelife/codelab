import os
import bsddb
import sys

dbFile = 'fileDB.db'
absoluteDBFile = os.getcwd()+'/'+dbFile

def listDir(rootPath):
    if os.path.exists(absoluteDBFile):
        os.remove(absoluteDBFile)
    
    db = bsddb.btopen(dbFile,'w')

    for root, dirs, files in os.walk(rootPath):
        print root
        for directory in dirs:
            if not root.endswith('/'):
                root += '/'
            db[root+directory] = directory
        for fi in files:
            db[root+fi] = fi

    db.close()

def search(keyWord):
	db = bsddb.btopen(dbFile, 'r')
	countAll = 0
	countResult=0
	for key, value in db.iteritems():
		countAll += 1
		if keyWord in value.lower():
			countResult += 1
			print value,'--->',key
	db.close()
	print 'All Num:', countAll
	print 'Result Num:',countResult
if __name__ == '__main__':
	if len(sys.argv) >= 3:
		if sys.argv[1] == '-l':
			listDir(sys.argv[2])
		elif sys.argv[1] == '-s':
			search(sys.argv[2])
	else:
		print 'Usage:python ftpSearchBasedOnBerkeleyDB.py -l[or -s] rootPath[or keyWord]'

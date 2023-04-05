import os
import os.path
import sys
from checksum import create_checksum

def diskwalk(path):
	filepaths=[]
	for root, dirs, files in os.walk(path):
		for file in files:
			print root+'/'+file
			filepaths.append(root+'/'+file)
	return filepaths

def findDupes(path=sys.argv[1]):
	print path
	dup = []
	record = {}
	d = diskwalk(path)
	print '*'*70
	for file in d:
		compound_key = (os.path.getsize(file),create_checksum(file))
		if compound_key in record:
			dup.append(file)
		else:
			record[compound_key]=file
	return dup

if __name__ == '__main__':
	dupes = findDupes()
	for dup in dupes:
		print "Duplicate: %s" %dup


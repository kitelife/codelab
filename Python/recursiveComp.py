import os
import sys

filesInDir1 = list()
filesInDir2 = list()

def recursiveCompare():
	if len(sys.argv) != 3:
		print 'Usage: python recursiveComp.py dir1 dir2'
	else:
		for root, dirs, files in os.walk(sys.argv[1]):
			for fi in files:
				filesInDir1.append(root+fi)
		for root, dirs, files in os.walk(sys.argv[2]):
			for fi in files:
				filesInDir2.append(root+fi)
		for item1 in filesInDir1:
			same = 0
			for item2 in filesInDir2:
				file1name = item1.split('/')[-1]
				file2name = item2.split('/')[-1]
				if file1name == file2name:
					same += 1
					print item1, item2
					command = "diff " + item1 + " " + item2
					os.system(command)
					filesInDir2.remove(item2)
			if same > 0 :
				filesInDir1.remove(item1)
		if len(filesInDir1) != 0:
			print filesInDir1
		if len(filesInDir2) != 0:
			print filesInDir2

if __name__ == '__main__':
	recursiveCompare()

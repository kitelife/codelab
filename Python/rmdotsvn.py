import os
import sys

for root, dirs, files in os.walk(sys.argv[1]):
	for dire in dirs:
		if dire == ".svn":
			print "rm -r %s"%(root+'/'+dire)
			os.popen("rm -r %s"%(root+'/'+dire))

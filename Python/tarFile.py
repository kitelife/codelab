#-*- coding: utf-8 -*-
#改编《Python for Unix and Linux Administration》示例6-18,用于打包音乐

import tarfile
import os
import fnmatch

tar = tarfile.open('music.tar','w')

for root, dir, files in os.walk('/home/xyf/Music'):
	for file in files:
		if fnmatch.fnmatch(file,'*.mp3'):
			fullpath = os.path.join(root,file)
			print fullpath
			tar.add(fullpath)

tar.close()

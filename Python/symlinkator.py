#-*- coding: utf-8 -*-
#!/usr/bin/python
'''
显示目录中的符号链接文件，其相应的实际文件位置，以及实际文件是否存在
'''

import os
import sys

def get_dir_tuple(filename,directory):
	abspath = os.path.join(directory, filename)
	realpath = os.path.realpath(abspath)
	exists = os.path.exists(abspath)
	return (filename, realpath, exists)

def get_links(directory):
	file_list = [get_dir_tuple(f,directory) for f in os.listdir(directory)
			if os.path.islink(os.path.join(directory, f))]
	return file_list

def main():
	if not len(sys.argv) == 2:
		print 'USAGE : %s directory' %sys.argv[0]
		sys.exit(0)
	directory = sys.argv[1]
	print get_links(directory)

if __name__ == '__main__':
	main()

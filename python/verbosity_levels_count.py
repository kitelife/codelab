#-*- coding:utf-8 -*-
#通过使用一个自动增加计数的设计模式，可以确保仅一个选项，却可以做三件不同的事情。
#如果使用'-v'，它设置options.verbose为1，如果使用'-vv'，它设置options.verbose为2。
#在实际的程序中，没有选项，仅输出文件名；使用'-v'将输出单词Filename以及文件名;使用
#'-vv'输出字节数以及文件名

import optparse
import os

def main():
	p = optparse.OptionParser(description="Python 'ls' command clone",
			prog="pyls",
			version="0.1a",
			usage="%prog [directory]")
	p.add_option("-v", action="count", dest="verbose")
	options, arguments = p.parse_args()
	if len(arguments) == 1:
		if options.verbose:
			print "Verbose Mode Enabled at Level: %s" % options.verbose
		path = arguments[0]
		for filename in os.listdir(path):
			if options.verbose==1:
				print "Filename: %s"%filename
			elif options.verbose==2:
				fullpath=os.path.join(path,filename)
				print "Filename: %s | Byte Size: %s" %(filename,
						os.path.getsize(fullpath))
			else:
				print filename
	else:
		p.print_help()

if __name__ == '__main__':
	main()

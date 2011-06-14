#-*- coding: utf-8 -*-

#"--quite"选项(该参数关闭所有标准输出)和"--verbose"选项(将触发额外输出)

import optparse
import os

def main():
	p = optparse.OptionParser(description="Python 'ls' command clone",
			prog="pyls",
			version="0.1a",
			usage="%prog [directory]"
			)
	p.add_option("--verbose",'-v',action="store_true",
			help="Enables Verbose Output",default=False)
	p.add_option("--quite",'-q',action="store_true",help="Enales quite",default=False)
	options, arguments = p.parse_args()
	print options, arguments

	if len(arguments) == 1:
		if options.verbose:
			print "Verbose Mode Enabled"
		path = arguments[0]
		for filename in os.listdir(path):
			if options.verbose:
				print "Filename: %s" % filename
			elif options.quite:
				pass
			else:
				print filename
	else:
		p.print_help()

if __name__ == "__main__":
	main()

import sys

num_arguments = len(sys.argv) - 1

if num_arguments == 0:
	sys.stderr.write('Hey, type in an option silly\n')
else :
	print sys.argv, "You typed in %s arguments"%num_arguments

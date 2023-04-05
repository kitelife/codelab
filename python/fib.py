import sys

def fib(n):
	print 'n = ', n
	if n > 1:
		return n * fib(n-1)
	else:
		print 'end of the line'
		return 1

if __name__ == '__main__':
	print fib(int(sys.argv[1]))

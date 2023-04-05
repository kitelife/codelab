import sys

def fabonacciRe(num):
	if num == 0:
		return 0
	elif num == 1:
		return 1
	else:
		return fabonacciRe(num-1)+fabonacciRe(num-2)

if __name__ == '__main__':
	print fabonacciRe(int(sys.argv[1]))


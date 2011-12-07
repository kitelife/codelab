#!/usr/bin/python

import sys

def fabonacciIter(num):
	first = 0
	second = 1
	number = 2

	while number <= num:
		result = first + second
		first = second
		second = result
		number += 1

	return (result,number)

if __name__ == '__main__':
	print fabonacciIter(int(sys.argv[1]))

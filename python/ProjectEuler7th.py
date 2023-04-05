'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''
from math import sqrt

number=2000000
count = 1

for i in range(2,number+1):
	marker = 0
	'''
	if i == number:
		number = number + 100
		print number
	'''
	for j in range(2,int(sqrt(i))+2):
		if i%j == 0:
			marker = marker + 1
			break
	if marker == 0:
		count = count + 1
	#print count
	if count == 10001:
		print i
		break
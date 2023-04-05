'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
from math import sqrt

sum=0

for number in range(2,2000000):
	marker = 0
	for i in range(2,int(sqrt(number))+1):
		if number % i ==0:
			marker = marker+1
			break
	if marker == 0:
		#print number
		sum = sum + number
print sum
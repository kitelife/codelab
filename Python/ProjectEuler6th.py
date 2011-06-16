'''
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
List1=[]
List2=[]

for number in range(1,101):
	List1.append(number*number)
	List2.append(number)
susq = sum(List1)
temp = sum(List2)
sqsu = temp*temp

print sqsu,'-',susq,'=',sqsu-susq
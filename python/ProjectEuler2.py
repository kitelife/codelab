#-*- encoding:utf-8 -*-
#Project Euler第二道题
FibonacciList = [1,2]
while FibonacciList[-1] <= 4000000:
	LastFirst=FibonacciList[-1]
	LastSecond=FibonacciList[-2]
	FibonacciList.append(LastFirst+LastSecond)
print FibonacciList
FibonacciList.pop()
print FibonacciList

allSum = 0
for number in FibonacciList:
	if (number%2)==0:
		allSum = allSum + number
print allSum


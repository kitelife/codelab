#!/usr/bin/python
#Filename:leapyear.py
#Author:youngsterxyf
#Time:2010.1.3.

def testYear(year):
	if not year%400:
		print '%s is leap year'%year
	elif (not year%4)and(year%100):
		print '%s is leap year'%year
	else:
		print '%s is not leap year'%year

year=raw_input('Plear Enter the year:')
year=int(year)
testYear(year)

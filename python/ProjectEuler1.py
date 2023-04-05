#-*- encoding:utf-8 -*-
#Project Euler第一道题

i = 1000/3+1
j = 1000/5
k = 1000/15+1
alllist = []
for multi in range(1,i):
	alllist.append(3*multi)
for multi in range(1,j):
	alllist.append(5*multi)
print alllist
allsum = sum(alllist)
print allsum
for multi in range(1,k):
	allsum = allsum - multi*15
print allsum
'''
allsum = 0
for multi in range(1,i):
	allsum = allsum +multi*3
print multi
print allsum

for multi in range(1,j):
	allsum = allsum+multi*5
print multi
print allsum
'''

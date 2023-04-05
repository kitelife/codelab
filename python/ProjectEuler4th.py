upBound = 999*999
downBound = 100*100
for number in range(upBound,downBound-1,-1):
	marker = 0
	strNumber = str(number)
	for index in range(0,len(strNumber)):
		if strNumber[index] != strNumber[-(index+1)]:
			marker=marker+1
			break
	if marker == 0:
		inmarker = 0
		for div in range(999,100,-1):
			quotient = number/div
			if number%div == 0 and quotient < 1000 and quotient >99:
				print div,'*',quotient,'=',number
				inmarker = inmarker + 1
				break
		if inmarker > 0:
			break
	if marker > 0:
		marker = 0
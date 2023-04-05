result = str(2**1000)
strLength= len(result)
sumOfDigits=0
for index in range(0,strLength):
	sumOfDigits = sumOfDigits + int(result[index])
print sumOfDigits

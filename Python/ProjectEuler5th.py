'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
def GCD(num1,num2):
	if num1 < num2:
		temp = num1
		num1=num2
		num2 = temp
	if num2==0:
		return num1
	else:
		return GCD(num2,num1%num2)
def LCM(num1,num2):
	temp=None
	temp = num1*num2/GCD(num1,num2)
	return temp

selectedNumList=[20,]
smallestProduct=1
for number in range(19,1,-1):
	listLength = len(selectedNumList)
	if listLength != 0:
		marker = 0
		for index in range(0,listLength):
			if selectedNumList[index]%number==0:
				marker = marker + 1
				break
		if marker == 0:
			selectedNumList.append(number)
#print len(selectedNumList)
Num =LCM(selectedNumList[0],selectedNumList[1])
for index in range(2,len(selectedNumList)):
	Num = LCM(Num,selectedNumList[index])

print Num


import sys

def fabonacci(num):
	resultList=[]
	for x in range(num+1):
		if x == 0:
			resultList.append(0)
		elif x == 1:
			resultList.append(1)
		else:
			resultList.append(resultList[x-1]+resultList[x-2])
	return resultList.pop()

if __name__ == '__main__':
	print fabonacci(int(sys.argv[1]))


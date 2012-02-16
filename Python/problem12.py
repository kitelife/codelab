symbol = True

result = 0

for i in range(1, 501):
	#print i
	result += i

number = 501

while symbol:
	result += number
	print '->', number
	print '--->', result
	number += 1
	count = 0
	if result % 2  == 0 :
		for i in range(2, result/2 + 1):
			if result % i == 0:
				count += 1
	elif result % 3 == 0:
		for i in range(3, result/3 + 1):
			if result % i == 0:
				count += 1
	elif result % 5 == 0:
		for i in range(5, result/5 + 1):
			if result % i == 0:
				count += 1
	elif result % 7 == 0:
		for i in range(7, result/7 + 1):
			if result % i == 0:
				count += 1
	else:
		for i in range(11, result/11 + 1):
			if result % i == 0:
				count += 1
	count += 2
	if count > 499:
		symbol = False
	print count
print result

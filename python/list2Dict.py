def list_to_dict(li):
	dct = {}
	for item in li:
		if dct.has_key(item):
			dct[item] = dct[item] + 1
		else:
			dct[item] = 1
	return dct

if __name__ == '__main__':
	li = [1, 1, 1, 2, 3, 3, 4, 4, 4, 4, 4, 5, 6, 7 ,7]
	print list_to_dict(li)

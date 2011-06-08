import os

for root,dir,files in os.walk(os.getcwd()):
	for fileName in os.listdir(root):
		if fileName.endswith('~') or fileName.endswith('.pyc') or fileName.endswith('.class'):
			filepath = root + '/' +fileName
			print filepath
			os.remove(filepath)

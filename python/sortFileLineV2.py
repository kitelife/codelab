#/usr/bin/python
#Version 0.2

ContentList=[]

f=open('cdays-4-test.txt')
content=f.readlines() #content is a list
f.close()
for line in content:
	line=line.replace('\n','')
	if len(line):
		if line.startswith('#'):
			continue
		line=line.lower()
		ListLine=line.split(' ')
		ListLine.sort()
		line=' '.join(ListLine)
		ContentList.append(line)

f=open('cdays-4-result.txt','w')
f.write('\n'.join(ContentList))
f.close()

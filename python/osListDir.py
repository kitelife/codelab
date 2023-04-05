import os
f=file('/home/xyf/cd.txt','a')
for root, dirs, files in os.walk('/media/Ubuntu 10.04 LTS i386'):
	f.write('%s %s %s\n'%(root,dirs,files))

f.close()

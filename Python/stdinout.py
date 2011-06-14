#-*- coding: utf-8 -*-

import subprocess
'''
注意subprocess与标准输入输出的交互
'''
p = subprocess.Popen('df -h',shell = True, stdout = subprocess.PIPE)
out = p.stdout.readlines()

for line in out:
	print line.strip()

print '*'*80

p = subprocess.Popen('wc -c',shell=True,stdin=subprocess.PIPE)
p.communicate('dadeqeqeq')

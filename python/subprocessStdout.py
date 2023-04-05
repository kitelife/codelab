#-*- coding: utf-8 -*-
#使用subprocess捕获标准输出

import subprocess

p = subprocess.Popen('df -h',shell = True, stdout = subprocess.PIPE)
out = p.stdout.readlines()

for line in out:
	print line.strip()

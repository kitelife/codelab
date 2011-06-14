#-*- coding : utf-8 -*-
'''
功能相当于命令 cat /etc/passwd | grep 0:0 | cut -d ':' -f 7
'''

import subprocess

p1 = subprocess.Popen('cat /etc/passwd',shell=True,stdout=subprocess.PIPE)
p2 = subprocess.Popen('grep 0:0',shell=True,stdin=p1.stdout,stdout=subprocess.PIPE)
p3 = subprocess.Popen('cut -d ":" -f 7',shell=True,stdin=p2.stdout,stdout=subprocess.PIPE)

print p3.stdout.read()

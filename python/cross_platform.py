#-*- coding: utf-8 -*-
'''文件名不能和库名相同，否则程序会将自己作为模块import，从而出错。因为在模块的搜索路径列表中当前目录是第一个
使用import sys
	sys.path
可查看模块的搜索列表
'''
#!/usr/bin/python

import platform

profile = {
'architecture':platform.architecture(),
'dist':platform.dist(),
'libc_ver':platform.libc_ver(),
'mac_ver':platform.mac_ver(),
'machine':platform.machine(),
'node':platform.node(),
'platform':platform.platform(),
'processor':platform.processor(),
'python_build':platform.python_build(),
'python_compiler':platform.python_compiler(),
'python_version':platform.python_version(),
'system':platform.system(),
'uname':platform.uname(),
'version':platform.version(),
}

for item in profile.items():
	print '%s : %s'%(item[0],item[1])

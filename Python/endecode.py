#-*- coding:utf-8 -*-
a=u'中文'
a_gb2312=a.encode('gb2312')
print a_gb2312

a_unicode=a_gb2312.decode('gb2312')
assert(a_unicode==a)

a_utf_8=a_unicode.encode('utf-8')
print a_utf_8


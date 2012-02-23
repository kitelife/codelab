#-*- coding: utf-8 -*-
#模块urllib中含有一个叫做urlopen的函数，其功能是打开目标网页，并返回一个类似于文件的
#对象，有了这个对象，我们就能像处理本地文件那样去处理网页数据了。

import urllib

url = "http://202.120.40.124"

web_page = urllib.urlopen(url)
for line in web_page:
    line = line.strip()
    print line
    
web_page.close()
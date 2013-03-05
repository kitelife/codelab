#!/usr/bin/python
#-*- coding: utf-8 -*-

'''
http://segmentfault.com/q/1010000000174694

Python如何将字符串转换成字典dict类型？
有下列字符串：
user = "{'name' : 'jim', 'sex' : 'male', 'age': 18}"
如何将字符串转换成字典dict类型？
'''

user = '{"name" : "jim", "sex" : "male", "age": 18}'

##################################################################################

# 1. 使用eval()或exec()函数实现

eval_user_info = eval(user)
print eval_user_info

exec('exec_user_info=' + user)
print exec_user_info

###################################################################################

# 2.这种字符串是典型的JSON格式，最好使用simplejson把JSON转化为Python内置类型
# JSON转化为字典
import simplejson

# JSON转化为字典
json_2_dict = simplejson.loads(user)
print json_2_dict

# 字典转化为JSON字符串
dict_2_jsonstr = simplejson.dumps(json_2_dict)
print dict_2_jsonstr

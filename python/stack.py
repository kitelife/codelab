#-*- coding: utf-8 -*-
class stack():
	'''
	简单地模拟栈功能
	'''
	def __init__(self):
		self.stack=list()
	def put(self,item):
		self.stack.append(item)
	def get(self):
		return self.stack.pop()

if __name__=='__main__':
	st=stack()
	i=3
	while(i>0):
		item=raw_input('Please input an item:')
		st.put(item)
		i-=1
	while(len(st.stack)):
		print len(st.stack)
		print st.get()

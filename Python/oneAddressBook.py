#!/usr/bin/python
#Filename:AddressBook.py
#Author:youngsterxyf
#Time:2011.1.2.

import sys 
import cPickle as p
import os

class person:
	def __init__(self,name):
		self.name=name
	def getName(self):
		return self.name

	def setPhone(self,phone):
		self.phone=phone
	def getPhone(self):
		return self.phone
	
	def setEmail(self,email):
		self.email=email
	def getEmail(self):
		return self.email
	def printInfo(self):
		print 'Name:%s Phone:%s Email:%s'%(self.name,self.phone,self.email)

personInfoDict={}

def addPerson():
	name=raw_input('Name:')
	Aperson=person(name)
	phone=raw_input('Phone:')
	Aperson.setPhone(phone)
	email=raw_input('Email:')
	Aperson.setEmail(email)
	personInfoDict[name]=Aperson

def showAllNames():
	for name in personInfoDict.keys():
		print name

def lookfor():
	name=raw_input('Please Enter the name:')
	if personInfoDict.has_key(name):
		person=personInfoDict.get(name)
		person.printInfo()
	else:
		print 'Sorry,there is no this person'

def remove():
	name=raw_input('Please Enter the name:')
	if personInfoDict.has_key(name):
		del personInfoDict[name]
		print 'Remove %s Successfully!'%name
	else:
		print 'Sorry,There is no this person'

def editPersonInfo():
	name=raw_input('Please Enter the name:')
	person=personInfoDict.get(name)
	while True:
		editWhat=raw_input('Which do you want to edit? -->')
		if editWhat=='email':
			email=raw_input('Email:')
			person.setEmail(email)
		elif editWhat=='Phone':
			phone=raw_input('Phone:')
			person.setPhone(phone)
		elif editWhat=='exit':
			personInfoDict[name]=person
			return

filePath='/home/xyf/Public/addressBook.txt'

attention='''
There is no person-Info,
Please add one or more
'''

if not os.path.exists(filePath):
	print attention
	addPerson()
else:
	f=file(filePath)
	personInfoDict=p.load(f)
	f.close()
	if len(personInfoDict)==0:
		print attention
		addPerson()
while True:
	tip='''
	what function do you want to select?
	1.Show all persons' name
	2.Look for some person's detail Info
	3.Remove some person
	4.add one person
	5.Edit some person
	6.Exit the program
	'''
	print tip

	select=raw_input('--->')
	if select=='1':
		showAllNames()
		continue
	elif select=='2':
		lookfor()
		continue
	elif select=='3':
		remove()
		continue
	elif select=='4':
		addPerson()
		continue
	elif select=='5':
		editPersonInfo()
		continue
	elif select=='6':
		f=file(filePath,'w')
		p.dump(personInfoDict,f)
		f.close()
		sys.exit()
	else:
		print 'Input error,Please select again!'

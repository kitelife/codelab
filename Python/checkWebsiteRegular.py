#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests
import sched
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

websites = {'http://www.test.com': 0}

MAILHOST = 'smtp.gmail.com:587'
MAILFROM = ""
MAILPASSWORD = ''
MAILTO = ''
SUBJECT = "服务器可能无法正常访问了"

def main():
	s = sched.scheduler(time.time, time.sleep)
	while 1:
		for url in websites.iterkeys():
			s.enter(5, 1, checkWebsite, (url,))
		s.run()
		for (website, failureCounter) in websites.iteritems():
			if failureCounter == 5:
				print 'failure'
				sendGmail(website + ' ===> ' '可能无法正常访问了，请赶紧检查')
				websites[website] = 0
			elif failureCounter == 0:
				print website, '===>', 'access successfully'
	
def checkWebsite(url):
	try:
		response = requests.head(url)
		if response.status_code != 200:
			websites[url] += 1
	except Exception, e:
		print e.message
		websites[url] += 1

def sendGmail(msg):
	mailto = MAILTO
	mailfrom = MAILFROM
	mailpassword = MAILPASSWORD
	mailhost = MAILHOST
	subject = SUBJECT
	
	email = MIMEText(msg, 'text', 'utf-8')
	email['Subject'] = Header(subject, 'utf-8')
	email['From'] = Header(mailfrom, 'utf-8')
	email['To'] = mailto
	try:
		s = smtplib.SMTP(mailhost)
		s.ehlo()
		s.starttls()
		s.ehlo()
		s.login(mailfrom, mailpassword)
		s.sendmail(mailfrom, mailto, email.as_string())
		s.quit()
	except Exception, e:
		print str(e)
	
if __name__ == '__main__':
	main()
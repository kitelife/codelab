#coding: utf-8

import hashlib
import json
import re
import random
from time import sleep

import requests


class Weixin:

	def __init__(self, username, password, login_url):
		self.username = username
		self.password = password
		self.md5_password = hashlib.md5(self.password).hexdigest()
		self.session = requests.Session()
		self.login_url = login_url
		self.token = ''
		self.user_list = []
	
	def fake_login(self):
		form_data = {
			'username': self.username,
			'pwd': self.md5_password,
			'imgcode': '',
			'f': 'json'
		}
		additional_headers = {
			'Origin': 'https://mp.weixin.qq.com',
			'Referer': 'https://mp.weixin.qq.com/',
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36'
		}
		r = self.session.post(self.login_url, data=form_data, headers=additional_headers)
		if r.status_code == 200:
			data = r.json()
			redirect_url = data['redirect_url']
			self.token = redirect_url.split('=')[-1]
			print self.token

	def parse_users(self):
		target_url = 'https://mp.weixin.qq.com/cgi-bin/contactmanage?t=user/index&pagesize=10&pageidx=0&type=0&token=%s&lang=zh_CN' %(self.token, )
		additional_headers = {
			'Referer': 'https://mp.weixin.qq.com/cgi-bin/home?t=home/index&lang=zh_CN&token=%s' %(self.token, ),
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36'
		}
		r = self.session.get(target_url, headers=additional_headers)
		users = None
		if r.status_code == 200:
			result = re.findall('friendsList\s*:\s*\((.+)\)\.contacts', r.content)
			if len(result):
				contacts = json.loads(result[0])
				users = contacts['contacts']
		if users:
			self.user_list = users
		print self.user_list


	def single_send(self, msg):
		target_url = 'https://mp.weixin.qq.com/cgi-bin/singlesend'
		for user in self.user_list:
			additional_headers = {
				'Origin': 'https://mp.weixin.qq.com', 
				'Referer': 'https://mp.weixin.qq.com/cgi-bin/singlesendpage?t=message/send&action=index&tofakeid=%s&token=%s&lang=zh_CN' %(user['id'], self.token),
				'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36',
				'X-Requested-With': 'XMLHttpRequest'
			}
			form_data = {
				'type': '1',
				'content': msg,
				'tofakeid': user['id'],
				'imgcode': '',
				'token': self.token,
				'lang': 'zh_CN',
				'random': random.random(),
				'f': 'json',
				'ajax': '1',
				't': 'ajax-response'
			}
			r = self.session.post(target_url, data=form_data, headers=additional_headers)
			if r.status_code == 200:
				print r.text
			sleep(2)


if __name__ == '__main__':
	wx = Weixin('xxx', 'xxx', 'https://mp.weixin.qq.com/cgi-bin/login?lang=zh_CN')
	wx.fake_login()
	sleep(1)
	wx.parse_users()
	sleep(1)
	wx.single_send(u'Hello, world!')

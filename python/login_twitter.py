#!/usr/bin/env python
#coding: utf-8

import requests
from BeautifulSoup import BeautifulSoup as BS

MAIN_URL = 'https://twitter.com'
LOGIN_URL = 'https://twitter.com/sessions'

PROXIES = {
    'http': '127.0.0.1:8087',
    'https': '127.0.0.1:8087'
}

USER_AGENT = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.172 Safari/537.22'


class login_twitter(object):

    def __init__(self, username, password):
        self.session = requests.Session()
        self.headers = {'User-Agent': USER_AGENT}
        self.username = username
        self.password = password
        self.token = None

    def get_token(self):
        r = self.session.get(MAIN_URL, headers = self.headers, proxies = PROXIES)
        print r.status_code
        twitter_soup = BS(r.text)
        token_ele = twitter_soup.find('input', attrs={'name': 'authenticity_token'})
        self.token = token_ele.get('value', None)

    def login_it(self):
        if self.token:
            payload = {
                'session[username_or_email]': self.username,
                'session[password]': self.password,
                'return_to_ssl': 'true',
                'scribe_log': '',
                'redirect_after_login': '/',
                'authenticity_token': self.token
            }
            r = self.session.post(LOGIN_URL, data = payload, headers = self.headers, proxies = PROXIES)
            print r.status_code
    

if __name__ == '__main__':

    login_instance = login_twitter('username', 'password')
    login_instance.get_token()
    login_instance.login_it()

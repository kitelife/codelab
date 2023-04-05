#!/usr/bin/python

import re, os
import requests
from BeautifulSoup import BeautifulSoup

INDEX_DICT = {'tw': (2, 12), 'dl': (36, 2), 'ga': (44, 1), 'wg': (46, 1), 'jp':
        (48, 1), 'yd': (49, 1)}
FORUM_URL_PATTERN = 'http://www.angnow.com/forum-%d-%d.html'

def parse_forum_x(forum_index):
    pages = forum_index[1]
    for page in xrange(1, pages+1):
        url = FORUM_URL_PATTERN %(forum_index[0], page)
        response = requests.get(url)
        if response.status_code == 200:
            page_soup = BeautifulSoup(response.content)
            mei_list = page_soup.findAll('a', attrs={'class': 'z', 'onclick': 'atarget(this)'})
            for mei in mei_list:
                mei_url = 'http://www.angnow.com/' + mei['href']
                parse_mei(mei_url)

def parse_mei(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        mei_soup = BeautifulSoup(resp.content)
        mei_pics = mei_soup.findAll('img', attrs={'id': re.compile('aimg_\d+'), 'aid':
            re.compile('\d+')})
        for pic in mei_pics:
            pic_url =  'http://www.angnow.com/' + pic['file']
            print pic_url
            download_pic(pic_url)

def download_pic(url):
    cmd = "wget %s" %url
    os.system(cmd)

def main():
    print INDEX_DICT
    for key, value in INDEX_DICT.iteritems():
        parse_forum_x(value)

if __name__ == '__main__':
    main()

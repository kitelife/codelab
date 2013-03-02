#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import requests
from BeautifulSoup import BeautifulSoup

def parse_class_x(class_name):
    last_page_num = 1
    base_url = 'http://qiip.net/category/firegirls/' + class_name
    resp = requests.get(base_url)
    if resp.status_code == 200:
        class_soup = BeautifulSoup(resp.content)
        last_page_element = class_soup.find('a', attrs={'title': u'跳转到最后一页'})
        if last_page_element:
            last_page_num = int(last_page_element['href'].split('/')[-1])
    
    for index in xrange(1, last_page_num+1):
        resp = requests.get(base_url + '/page/' + str(index))
        if resp.status_code == 200:
            page_soup = BeautifulSoup(resp.content)
            zm_entry_list = page_soup.findAll('div', attrs={'class': 'entry box-info'})
            for zm_entry in zm_entry_list:
                zm_url = zm_entry.find('a')['href']
                download_zm_pics(zm_url)

def download_zm_pics(zm_url):
    resp = requests.get(zm_url)
    if resp.status_code == 200:
        zm_soup = BeautifulSoup(resp.content)
        target_part = zm_soup.find('div', attrs={'class': 'entry clearfix'})
        if target_part:
            pic_element_list = target_part.findAll('a')
            for pic_element in pic_element_list:
                pic_url = pic_element.get('href', None)
                if pic_url:
                    os.system('wget %s' %pic_url)

def main():
    class_list = ['breast', 'pure', 'legs']
    for class_x in class_list:
        parse_class_x(class_x)

if __name__ == '__main__':
    main()

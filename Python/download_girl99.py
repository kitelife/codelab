#!/usr/bin/env python
#coding: utf-8

import re
import os
import requests

main_url = 'http://girl99.pixnet.net'
albumlist_url = 'http://girl99.pixnet.net/album/list'

PROXIES = {
        'http': '127.0.0.1:8087',
        'https': '127.0.0.1:8087'
    }

ALL_ALBUM_LIST = []

def parse_album_list(url):
    content = download_content(url)
    albumurl_pattern = re.compile('<a\s+class="photolink"\s+href="(http://girl99\.pixnet.net/album/set/\d+#?(?:after=\d+)?)">')
    album_urls = albumurl_pattern.findall(content)
    print len(album_urls)
    ALL_ALBUM_LIST.extend(album_urls)
    next_pageurl_pattern = re.compile('<a\s+class="nextBtn"\s+href="(/album/list\?after=\d+)">')
    may_next_page = next_pageurl_pattern.findall(content)
    if len(may_next_page):
        print 'next_page: %s' %may_next_page[0]
        nextpage_url = main_url + may_next_page[0]
        parse_album_list(nextpage_url)


def parse_album(url):
    photo_urls = []
    
    content = download_content(url)
    def parse_onepage(page_content):
        photo_pattern = re.compile('<a\s+class="photolink"\s+title="\d+"\shref="(http://girl99.pixnet.net/album/photo/\d+(?:#after=\d+)?)">')
        onepage_photos = photo_pattern.findall(page_content)
        photo_urls.extend(onepage_photos)
        nextpage_pattern = re.compile('<a\sclass="nextBtn"\s+href="(/album/set/\d+\?after=\d+)">')
        may_nextpage = nextpage_pattern.findall(page_content)
        if len(may_nextpage):
            print '### next_page: %s' %may_nextpage[0]
            nextpage_url = main_url + may_nextpage[0]
            nextpage_content = download_content(nextpage_url)
            parse_onepage(nextpage_content)

    albumname_pattern = re.compile('<meta\s+name="description"\s+content="girl99\s+的相簿\s+-\s+(.+)">')
    may_albumname = albumname_pattern.findall(content)
    albumname = 'xxx'
    if len(may_albumname):
        albumname = may_albumname[0].replace(' ', '_').replace('/', '')
    parse_onepage(content)
    if not os.path.exists(albumname):
        os.mkdir(albumname)
    print albumname
    albumname += '/'
    for photo_url in photo_urls:
        download_photo(albumname, photo_url)


def download_photo(dir_name, url):
    content = download_content(url)
    url_for_download_pattern = re.compile('<meta\s+name="twitter:image"\s+content="(http://pic\.pimg\.tw/girl99/\d+-\d+\.jpg)">')
    may_url_for_download = url_for_download_pattern.findall(content)
    url_for_download = None
    if len(may_url_for_download):
        url_for_download = may_url_for_download[0]
    print url_for_download
    if url_for_download:
        photo_name = url_for_download.split('/')[-1]
        photo = download_content(url_for_download)
        photo_path = dir_name + photo_name
        with open(photo_path, 'wb') as fh:
            fh.write(photo)


def download_content(url):
    content = ''
    r = requests.get(url, proxies = PROXIES)
    if r.status_code == requests.codes.OK:
        content = r.content
    return content

def main():
    parse_album_list(albumlist_url)
    for album_url in ALL_ALBUM_LIST:
        parse_album(album_url)

if __name__ == '__main__':
    main()

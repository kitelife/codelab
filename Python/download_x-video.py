#!/usr/bin/env python
#coding: utf-8

import sys
import re
import urllib
import requests

PROXIES = {
        'http': '127.0.0.1:8087',
        'https': '127.0.0.1:8087'
        }


class Downloader(object):

    def __init__(self, url):
        self.url = url
        self.session = requests.Session()
        self.target_url = ''
        self.video_name = ''

    def _parse_target_url(self):
        r = self.session.get(self.url, proxies=PROXIES)
        if r.status_code == requests.codes.OK:
            url_pattern = re.compile('flv_url=(http.+)&amp;url_bigthumb')
            maybe_target_url = url_pattern.findall(r.text)
            if len(maybe_target_url) == 1:
                self.target_url = maybe_target_url[0]
            videoname_pattern = re.compile('<meta\s+name="description"\s+content="([\w\s]+)">')
            maybe_videoname = videoname_pattern.findall(r.text)
            if len(maybe_videoname) == 1:
                video_name = maybe_videoname[0]
                self.video_name = '{0}.flv'.format(video_name.replace(' ', '_').replace('/', ''))

    def download_video(self):
        self._parse_target_url()
        self.target_url = urllib.unquote(self.target_url)
        print self.target_url
        r = self.session.get(self.target_url, stream=True, proxies=PROXIES)
        print str(int(r.headers['content-length']) / 1024 / 1024) + 'MB'
        print r.headers['content-type']
        if r.status_code == requests.codes.OK:
            with open(self.video_name, 'wb') as fh:
                now_len = 0
                show_len = 0
                for part_content in r.iter_content(chunk_size=1024):
                    now_len += 1024
                    if now_len % (1024 * 1024) == 0:
                        show_len += 1
                        print str(show_len) + 'MB'
                    fh.write(part_content)


def main():
    downloader = Downloader(sys.argv[1])
    downloader.download_video()

if __name__ == '__main__':
    '''x-video-s'''
    main()

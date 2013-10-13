#!/usr/bin/env python
#coding: utf-8

import sys
import re
import urllib
import requests

PROXIES = {
        'http': 'http://127.0.0.1:8087',
        'https': 'http://127.0.0.1:8087'
        }


class Downloader(object):

    def __init__(self, url):
        self.url = url
        self.session = requests.Session()
        self.target_url = ''
        self.video_name = ''

    def _parse_target_url(self):
        print self.url
        r = self.session.get(self.url, proxies=PROXIES)
        if r.status_code == requests.codes.OK:
            url_pattern = re.compile('flv_url=(http.+)&amp;url_bigthumb')
            maybe_target_url = url_pattern.findall(r.text)
            if len(maybe_target_url) == 1:
                self.target_url = maybe_target_url[0]
            videoname_pattern = re.compile('<meta\s+name="description"\s+content="(.+)">')
            maybe_videoname = videoname_pattern.findall(r.text)
            if len(maybe_videoname) == 1:
                video_name = maybe_videoname[0]
                new_video_name = video_name.replace(' ', '_').replace('/', '')
                self.video_name = '%s.flv'%new_video_name.encode('utf-8').decode('utf-8')

    def download_video(self):
        self._parse_target_url()
        self.target_url = urllib.unquote(self.target_url)
        r = self.session.get(self.target_url, stream=True, proxies=PROXIES)
        total_size = int(r.headers['content-length'])
        percent_one_size = total_size / 50
        #print self.video_name
        print str(total_size / 1024 / 1024) + 'MB'
        if r.status_code == requests.codes.OK:
            print '[',
            sys.stdout.flush()
            with open(self.video_name, 'wb') as fh:
                for part_content in r.iter_content(chunk_size=percent_one_size):
                    print '=',
                    sys.stdout.flush()
                    fh.write(part_content)
            print ']'
            sys.stdout.flush()


def main():
    downloader = Downloader(sys.argv[1])
    downloader.download_video()

if __name__ == '__main__':
    '''x-video-s'''
    main()

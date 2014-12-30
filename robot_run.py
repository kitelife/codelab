# coding: utf-8

__author__ = 'xiayongfeng'

import sys
import time
import multiprocessing
import platform
import re

import requests
from pyquery import PyQuery as pq


def __get_platform_encoding():
    platform_encoding = 'utf-8'
    if platform.system() not in ['Linux', 'Darwin']:
        platform_encoding = 'gbk'
    return platform_encoding


def vote(seq_id):
    print 'Seq_id: ', seq_id
    platform_encoding = __get_platform_encoding()
    count = 1
    while True:
        form_hash = -1
        s = requests.session()
        http_get_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36',
            'Host': 'www.51pretty.net'
        }
        try:
            r = s.get('http://www.51pretty.net/plugin.php?id=chs_threadvote:vote', headers=http_get_headers, timeout=15)
        except Exception as e:
            print 'Exception: ', e
            continue
        if r.status_code != 200:
            print 'status_code: ', r.status_code
            continue
        dom_pq = pq(r.text)
        form_hash = dom_pq.find('#formhash').attr.value
        print 'form_hash:', form_hash
        continue_my_loop = True
        while continue_my_loop:
            print count
            pay_load = {
                'check[8]': '1',
                'formhash': form_hash,
                'commitvote': u'提交投票'
            }
            http_post_headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'www.51pretty.net',
                'Origin': 'http://www.51pretty.net',
                'Referer': 'http://www.51pretty.net/plugin.php?id=chs_threadvote:vote',
            }
            url = 'http://www.51pretty.net/plugin.php?id=chs_threadvote:vote&infloat=1&inajax=1'
            try:
                r = s.post(url, data=pay_load, headers=http_post_headers, timeout=15)
            except Exception as e:
                print 'Error: ', e
                continue_my_loop = False
                continue
            if r.status_code != 200:
                print 'status_code: ', r.status_code
                continue_my_loop = False
                continue
            try:
                print r.text.encode(platform_encoding)
            except Exception as e:
                print 'Error: ', e
            # 投票成功的响应结果中有right字符串
            has_it = re.search('right', r.text)
            if has_it is None:
                continue_my_loop = False
                continue
            count += 1
            time.sleep(1)
        time.sleep(1)

def main():
    if len(sys.argv) != 2:
        print 'please run it with two arguments'
        return
    process_records = []
    for seq_id in xrange(1, int(sys.argv[1]) + 1):
        new_process = multiprocessing.Process(target=vote, args=(seq_id,))
        new_process.start()
        process_records.append(new_process)
    
    for pr in process_records:
        pr.join()
        
if __name__ == '__main__':
    main()

'''
<?xml version="1.0" encoding="gbk"?>
<root><![CDATA[<script type="text/javascript" reload="1">if(typeof errorhandle_commitvote=='function') {errorhandle_commitvote('投票成功！', {});}hideWindow('commitvote');showDialog('投票成功！', 'right', null, null, 0, null, null, null, null, 1, null);</script><script>showWindow("enterinfo","plugin.php?id=chs_threadvote:info&vid=527556");</script>]]></root>
'''

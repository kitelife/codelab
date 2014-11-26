# coding: utf-8

__author__ = 'xiayongfeng'

import time

import requests
from pyquery import PyQuery as pq


def main():
    s = requests.session()
    r = s.get('http://www.51pretty.net/plugin.php?id=chs_threadvote:vote')
    if r.status_code != 200:
        print 'status_code:', r.status_code
    dom_pq = pq(r.text)
    form_hash = dom_pq.find('#formhash').attr.value
    print 'form_hash:', form_hash
    count = 1
    while True:
        print count

        pay_load = {
            'check[8]': '1',
            'formhash': form_hash,
            'commitvote': u'提交投票'
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'www.51pretty.net',
            'Origin': 'http://www.51pretty.net',
            'Referer': 'http://www.51pretty.net/plugin.php?id=chs_threadvote:vote',
        }
        url = 'http://www.51pretty.net/plugin.php?id=chs_threadvote:vote&infloat=1&inajax=1'
        r = s.post(url, data=pay_load, headers=headers)
        print r.status_code
        print r.text

        time.sleep(1)
        count += 1

if __name__ == '__main__':
    main()

'''
<?xml version="1.0" encoding="gbk"?>
<root><![CDATA[<script type="text/javascript" reload="1">if(typeof errorhandle_commitvote=='function') {errorhandle_commitvote('投票成功！', {});}hideWindow('commitvote');showDialog('投票成功！', 'right', null, null, 0, null, null, null, null, 1, null);</script><script>showWindow("enterinfo","plugin.php?id=chs_threadvote:info&vid=527556");</script>]]></root>
'''
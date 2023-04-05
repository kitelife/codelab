#!/usr/bin/env python
#coding: utf-8

import platform
import socket
import urllib2
import argparse
import time
import sys

def get_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', action="store", default="https://smarthosts.googlecode.com/svn/trunk/hosts", 
            help="The url where hosts content comes from")
    parser.add_argument('-t', action="store", default="C:\Windows\System32\drivers\etc\hosts", 
            help="The absolute path which locates the hosts file")
    parser.add_argument('-d', action="store", default=None, 
            help="the file contains those hosts always needed")
    
    return parser

def main():
    parser = get_argparser()
    args = parser.parse_args()
    
    source_url = args.u
    target_host_path = args.t
    default_hosts_file = args.d

    source_hosts = ''
    try:
        response = urllib2.urlopen(source_url)
        source_hosts = response.read()
    except urllib2.URLError:
        print "源hosts网址有误"
    except urllib2.HTTPError:
        print "网络访问失败"
    except:
        print "发生错误"

    if source_hosts:
        update_time = time.ctime()
        hostname = socket.gethostname()
        hosts_content = '# ' + update_time + "\n127.0.0.1\t" + hostname + "\n"
        
        if default_hosts_file:
            try:
                with open(default_hosts_file, 'r') as fh:
                    hosts_content += fh.read() + "\n"
            except:
                print "failed to open the file contains those hosts always needed"
        hosts_content += source_hosts

        if platform.system() in ['Linux', 'Darwin']:
            target_host_path = '/etc/hosts'
        try:
            with open(target_host_path, 'w') as fh:
                fh.write(hosts_content)
        except:
            print '无法成功写hosts'
            sys.exit(1)

        print "成功更新hosts"
    else:
        print "未能成功更新hosts"

if __name__ == '__main__':
    main()

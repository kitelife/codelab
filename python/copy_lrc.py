#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import sys

DST_DIR = '/home/xiayf/.lyrics/'

def copy_lrc(src_dir_name):
    files = os.listdir(src_dir_name)
    for f_d in files:
        f_d = src_dir_name + '/' + f_d
        if os.path.isdir(f_d):
            copy_lrc(f_d)
        if os.path.isfile(f_d):
            if f_d.endswith('.lrc'):
                filename = f_d.split('/')[-1]
                with open(f_d, 'r') as fh_s:
                    content = fh_s.read()
                    with open(DST_DIR + filename, 'w') as fh_d:
                        fh_d.write(content)
                print f_d
if __name__ == '__main__':
    src_dir = sys.argv[1]
    if len(sys.argv) > 2:
        DST_DIR = sys.argv[2]
    copy_lrc(src_dir)

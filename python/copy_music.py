#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import sys

DST_DIR = '/home/xiayf/Music/单曲/'

def copy_lrc(src_dir_name):
    files = os.listdir(src_dir_name)
    for f_d in files:
        f_d = src_dir_name + '/' + f_d
        if os.path.isdir(f_d):
            copy_lrc(f_d)
        if os.path.isfile(f_d):
            if f_d.endswith('.mp3'):
                filename = f_d.split('/')[-1]
                with open(f_d, 'rb') as fh_s:
                    content = fh_s.read()
                    with open(DST_DIR + filename, 'wb') as fh_d:
                        fh_d.write(content)
                print f_d
if __name__ == '__main__':
    src_dir = sys.argv[1]
    if len(sys.argv) > 2:
        DST_DIR = sys.argv[2]
    copy_lrc(src_dir)

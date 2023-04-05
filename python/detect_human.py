#!/usr/bin/python
#-*-coding: utf-8 -*-

import os, sys
from SimpleCV import *

template = 'face'
output_dir = '/home/usrname/output/'

def handle_pics(dir_name):
    files = os.listdir(dir_name)
    for f_d in files:
        f_d = dir_name + '/' + f_d
        if os.path.isdir(f_d):
            handle_pics(f_d)
        if os.path.isfile(f_d):
            pic_detect(f_d)

def pic_detect(file_name):
    haar_cascade = HaarCascade(template)
    image_object = None
    try:
        image_object = Image(file_name)
    except Exception:
        print file_name + ' 不是图片?'
    if image_object:
        targets = None
        try:
            targets = image_object.findHaarFeatures(haar_cascade)
        except Exception:
            pass
        if targets:
            print file_name
            biggest_area = 15000
            for t_a in targets.area():
                if t_a > biggest_area:
                    biggest_area = t_a
            if biggest_area > 15000:
                #targets.show()
                with open(file_name, 'rb') as fh_s:
                    outputfile_name = output_dir + file_name.split('/')[-1]
                    print outputfile_name
                    with open(outputfile_name, 'wb') as fh_d:
                        fh_d.write(fh_s.read())

def main():
    arg_len = len(sys.argv)
    if arg_len < 2:
        print 'usage: python detect.py pics_dir [detect_what]'
        return
    dir_name = sys.argv[1]
    global template
    if len(sys.argv) == 3:
        template = sys.argv[2]
    handle_pics(dir_name)

if __name__ == '__main__':
    main()

#!/usr/bin/python

import os, sys

target_dir = 'output/'

def rename_files(dir_name):

    if not dir_name.endswith('/'):
        dir_name += '/'
    file_names = os.listdir(dir_name)
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    name_template = '%s.%s'
    count = 1
    for filename in file_names:
        if not filename.startswith('.'):
            file_type = filename.split('.')[-1]
            new_name = target_dir + name_template %(str(count), file_type)
            print filename, '--->', new_name
            os.system('cp "%s" "%s"' %(dir_name + filename, new_name))
            count +=1

if __name__ == '__main__':
    arg_len = len(sys.argv)
    if arg_len != 2:
        print 'usage: python rename_all.py dir_name'
    else:
        rename_files(sys.argv[1])

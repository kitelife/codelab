#!/usr/bin/python

import os, sys

def rename_files(dir_name):

    if not dir_name.endswith('/'):
        dir_name += '/'

    file_names = os.listdir(dir_name)
    try:
        file_names.remove('.')
        file_names.remove('..')
    except Exception:
        pass
    name_template = '%s.%s'
    count = 1
    for filename in file_names:
        file_type = filename.split('.')[-1]
        new_name = dir_name + name_template %(str(count), file_type)
        print filename, '--->', new_name
        os.rename(dir_name + filename, new_name)
        count +=1 

if __name__ == '__main__':
    arg_len = len(sys.argv)
    if arg_len != 2:
        print 'usage: python rename_all.py dir_name'
    else:
        rename_files(sys.argv[1])

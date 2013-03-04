#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import sys
import re
import json
import matplotlib.pyplot as plt

count_dict = {}
for_type_merge = {'C source': 'c', 'Perl script': 'pl', 
                    'Python script': 'py', 'POSIX shell script': 'sh',
                    'C++ source': 'cpp', 'LaTeX document': 'tex',
                    'Bourne-Again shell script': 'sh', 
                    'XML document text': 'xml', 'PHP script': 'php',
                    'JPEG image data': 'jpeg', 'HTML document': 'html',
                    'PDF document': 'pdf', 'Zip archive data': 'zip',
                    'awk script': 'awk'}
json_filename = 'files_count.json'

def count_files(dir_name):
    dir_name = os.path.abspath(dir_name)
    dir_name += '/'
    file_list = os.listdir(dir_name)
    try:
        file_list.remove('.')
        file_list.remove('..')
    except Exception:
        pass
    regex = '\w{1,4}\Z'
    filetype_file_output = for_type_merge.keys()

    for file_name in file_list:
        if not file_name.startswith('.'):
            absolute_file_name = dir_name + file_name
            if os.path.isdir(absolute_file_name):
                count_files(absolute_file_name)
            else:
                file_type = ''
                maybe_filetype = file_name.split('.')[-1].lower()
                if re.match(regex, maybe_filetype):
                    file_type = maybe_filetype.lower()
                else:
                    cmd = 'file "%s"' %absolute_file_name
                    file_cmd_out = os.popen(cmd).read()
                    file_type = file_cmd_out.split(':')[1].split(',')[0].strip(' ').strip('\n').lower()
                    if file_type in filetype_file_output:
                        file_type = for_type_merge[file_type]
                print file_type
                count_dict[file_type] = count_dict.get(file_type, 0) + 1


'''
def dict_to_twolevellist(some_dict):
    return [[key, value] for key, value in some_dict.iteritems()]
'''
'''
def twolevellist_to_dict(some_list):
    return {key: value for [key, value] in some_list}
'''

def sort_dict_by_value(some_dict, r=False):
    return sorted(some_dict.items(), key=lambda some_dict: some_dict[1], reverse=r)

def dump_files_count(some_dict, json_file):
    with open(json_file, 'w') as json_file_handler:
        json_file_handler.write(json.dumps(some_dict))

'''
def json_to_txt(json_file, txt_file):
    filetype_count = None
    with open(json_file, 'r') as f_h:
        filetype_count = json.loads(f_h.read())
    with open(txt_file, 'w') as f_h:
        for key, value in filetype_count.iteritems():
            f_h.write(key + '\t' + str(value) + '\n')
'''

def visual_with_matplotlib(count_dict):
    count_list = sort_dict_by_value(count_dict, True)
    
    labels = None
    values = None
    if len(count_list) > 20:
        labels = ['' for _ in xrange(20)]
        values = [0 for _ in xrange(20)] 
        labels[19] = 'others'
        for index, item in enumerate(count_list):
            if index < 19:
                labels[index] = item[0]
                values[index] = item[1]
            else:
                values[19] += item[1]
    else:
        labels = []
        values = []
        for index, item in enumerate(count_list):
            labels.append(item[0])
            values.append(item[1])
            
    plt.pie(values, labels=labels)
    plt.show()

if __name__ == '__main__':
    if '-c' in sys.argv:
        dir_name = sys.argv[1]
        count_files(dir_name)
        dump_files_count(count_dict, json_filename)
    visual_with_matplotlib(json.loads(open(json_filename, 'r').read()))

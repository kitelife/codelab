#!/usr/bin/python
#-*- coding: utf-8 -*-
'''
从一个Git版本库的工作目录中拷贝代码文件（除了.git目录外的其他目录文件到别处）
因为还不熟悉Git的用法，才写了这个脚本，Git应该有仅签出代码文件的功能
'''

import sys
import os

base_dir = ''

def copy_without_dotgit(repos_dir, target_parent_dir):
    if not repos_dir.endswith('/'):
        repos_dir += '/'
    print repos_dir
    entry_list = os.listdir(repos_dir)
    for entry in entry_list:
        entry_path = repos_dir + entry
        if entry != '.git':
            if os.path.isdir(entry_path):
                target_dirname = entry_path.replace(base_dir, '').strip('/')
                target_dirname = target_parent_dir + target_dirname
                cmd = 'mkdir "%s"' %target_dirname
                os.system(cmd)
                copy_without_dotgit(entry_path, target_parent_dir)
            elif os.path.isfile(entry_path):
                target_filename = entry_path.replace(base_dir, '').strip('/')
                target_filename = target_parent_dir + target_filename
                cmd = 'cp "%s" "%s"' %(entry_path, target_filename)
                os.system(cmd)
        else:
            pass

def main():
    if len(sys.argv) != 3:
        print "usage: python copy_pure_git_repos.py source_repos_dir target_dir"
        return
    repos_dir = sys.argv[1]
    target_dir = os.path.abspath(sys.argv[2]) + '/'
    global base_dir
    base_dir = repos_dir
    copy_without_dotgit(repos_dir, target_dir)

if __name__ == '__main__':
    main()

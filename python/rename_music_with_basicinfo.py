#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''

author: youngsterxyf<sas.198708@gmail.com>

该脚本用于抽取音乐文件的基本信息，然后根据这些基本信息对文件进行重命名

'''

import sys
import os
from mutagen.id3 import ID3

def parse_info(music_path):
    audio = ID3(music_path)
    music_name = audio.get('TIT2', '')
    if music_name:
        music_name = music_name.pprint().split('=')[-1]
    album_name = audio.get('TALB', '')
    if album_name:
        album_name = album_name.pprint().split('=')[-1]
    singer = audio.get('TPE1', '')
    if singer:
        singer = singer.pprint().split('=')[-1]
    return [music_name, singer, album_name]


def traverse_music_dir(dir_name):
    if not dir_name.endswith('/'):
        dir_name += '/'
    file_list = os.listdir(dir_name)
    for f in file_list:
        abs_path = dir_name + f
        if os.path.isdir(abs_path):
            traverse_music_dir(abs_path)
        elif abs_path.endswith('.mp3'):
            print abs_path
            parse_music_and_rename(abs_path)
        else:
            continue

def parse_music_and_rename(music_path):
    music_info = parse_info(music_path)
    if not music_info[0]:
        pass
    else:
        if '' in music_info:
            music_info.remove('')
        new_name = '-'.join(music_info) + '.mp3'
        new_name = '{0}/{1}'.format('/'.join(music_path.split('/')[:-1]), new_name.encode('utf-8'))
        try:
            os.rename(music_path, new_name)
        except Exception:
            pass


if __name__ == '__main__':
    music_path = sys.argv[1]
    if os.path.isdir(music_path):
        traverse_music_dir(music_path)
    elif music_path.endswith('.mp3'):
        parse_music_and_rename(music_path)
    else:
        pass

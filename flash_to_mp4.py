# coding: utf-8

import os
import sys
import os.path
import time

cwd = os.getcwd()

def load_ts_list(chunklist_filename):
    with open(chunklist_filename) as fh:
        ts_list = []
        for line in fh:
            line = line.strip()
            if line.startswith('#'):
                continue
            if len(line) == 0:
                continue
            ts_list.append(line)
        return ts_list

def check_ts_list(ts_list):
    exist_ts_list = []
    for ts in ts_list:
        if not os.path.exists(os.path.join(cwd, ts)):
            continue
        exist_ts_list.append(ts)
    return exist_ts_list


def main():
    chunklist_filename = sys.argv[1]
    # 解析出ts文件列表
    ts_list = load_ts_list(chunklist_filename)
    # 检测哪些ts文件已经下载
    checked_ts_list = check_ts_list(ts_list)

    # 如果已经下载了部分ts文件，则直接转换合并，否则先逐个下载ts文件
    if len(checked_ts_list) == 0:
        base_url = sys.argv[2]
        for ts in ts_list:
            cmd = 'wget {resource}'.format(resource=base_url + ts)
            os.system(cmd)
    else:
        ts_list = checked_ts_list

    # ts 转换合并为 mp4
    cmd = 'ffmpeg -i "concat:{tss}" -acodec copy -vcodec copy -absf aac_adtstoasc {out_file_name}.mp4'.format(tss='|'.join(ts_list),
        out_file_name=time.time())
    os.system(cmd)

    # 清理
    for ts in ts_list:
        os.remove(os.path.join(cwd, ts))
    os.remove(os.path.join(chunklist_filename))

if __name__ == '__main__':
    main()

# coding: utf-8

import os
import sys


def load_ts_list():
    with open(sys.argv[1]) as fh:
        ts_list = []
        for line in fh:
            line = line.strip()
            if line.startswith('#'):
                continue
            if len(line) == 0:
                continue
            ts_list.append(line)
        return ts_list


def main():
    base_url = sys.argv[2]
    ts_list = load_ts_list()
    for ts in ts_list:
        cmd = 'wget {resource}'.format(resource=base_url + ts)
        os.system(cmd)
    cmd = 'ffmpeg -i "concat:{tss}" -acodec copy -vcodec copy -absf aac_adtstoasc output.mp4'.format(tss='|'.join(ts_list))
    os.system(cmd)

if __name__ == '__main__':
    main()

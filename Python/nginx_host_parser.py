#coding: utf-8

import sys
import re

CONF_DIR = './'


class Log():
    '''
    日志类
    '''

    def __init__(self, logfile_path):
        self.fh = open(logfile_path, 'w')

    def write_log(self, content):
        self.fh.write(content)

    def close_log(self):
        self.fh.close()


def merge_multispace_one(input_str):
    return ' '.join(filter(lambda x: x, input_str.split()))


def parse_host_conf(conf_file_path):
    server_pattern = r'(\s*server\s*\n*{(?:[^{}]+{(?:[^{}]+|(?:[^{}]*{[^{}]+}[^{}]*)+)})+\n*\s*})|(\s*server\s*\n*{[^{}]+})'
    server_regex_obj = re.compile(server_pattern)

    servername_pattern = r'\s*server_name\s*([^;]+)\s*;'
    servername_obj = re.compile(servername_pattern)

    proxy_pass_pattern = r'\s*proxy_pass\s*([^;]+)\s*;'
    proxy_pass_obj = re.compile(proxy_pass_pattern)

    with open(conf_file_path, 'r') as fh:
        content = fh.read()
        server_list = server_regex_obj.findall(content)
        count = 0
        logger = Log('output.log')
        domain_upstream = []
        for server in server_list:
            selection = filter(lambda x:x, map(lambda x:x.strip(), server))
            selection = selection[0]
            logger.write_log(selection + '\n')
            logger.write_log('*' * 80 + "\n\n")
            server_name_s = merge_multispace_one(' '.join(servername_obj.findall(selection)))
            logger.write_log('server_name: ' + server_name_s + '\n')
            proxy_pass_s = merge_multispace_one(' '.join(proxy_pass_obj.findall(selection)))
            logger.write_log('proxy_pass: ' + proxy_pass_s + '\n')
            count += 1
            if server_name_s != '' and proxy_pass_s != '':
                domain_upstream.append([proxy_pass_s.split(' '), server_name_s.split(' ')])
        print domain_upstream
        print len(domain_upstream)

        logger.write_log(str(count) + "\n")
        logger.close_log()


if __name__ == '__main__':
    conf_file_path = CONF_DIR + 'host.conf'
    if len(sys.argv) > 1:
        conf_file_path = sys.arv[1]

    parse_host_conf(conf_file_path)

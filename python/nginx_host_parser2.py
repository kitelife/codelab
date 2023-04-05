#coding: utf-8

import sys


def parse_host_conf(conf_file_path):
    stack_for_braces = []
    results_list = []
    with open(conf_file_path, 'r') as fh:
        content = fh.readlines()
        server_begin_flag = True
        for line in content:
            line = line.strip()
            if line.startswith('server '):
                if len(stack_for_braces):
                    print "配置文件有错误"
                    sys.exit(1)
                else:
                    server_begin_flag = True
                    results_list.append({})
            if line.startswith('server_name') or line.startswith('proxy_pass'):
                line = line.rstrip(';')
                line_parts = line.split()
                line_parts = filter(lambda x:x, map(lambda x:x.strip(), line_parts))
                target_list = line_parts[1:]
                if line.startswith('server_name'):
                    results_list[-1]['server_name'] = target_list
                else:
                    if results_list[-1].has_key('proxy_pass'):
                        results_list[-1]['proxy_pass'].extend(target_list)
                    else:
                        results_list[-1]['proxy_pass'] = target_list

            for char in line:
                if char == '{':
                    stack_for_braces.append(char)
                    if server_begin_flag:
                        server_begin_flag = False
                if char == '}':
                    if len(stack_for_braces) and (stack_for_braces[-1] == '{'):
                        stack_for_braces.pop()
                    else:
                        print "配置文件有错误"
                        sys.exit(1)
                    if server_begin_flag:
                        print "配置文件有错误"
                        sys.exit(1)

    print stack_for_braces
    for item in results_list:
        print item
    print len(results_list)


if __name__ == '__main__':
    conf_file_path = './host.conf'
    if len(sys.argv) > 1:
        conf_file_path = sys.argv[1]
    parse_host_conf(conf_file_path)

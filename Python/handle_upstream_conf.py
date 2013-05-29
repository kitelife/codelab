#coding: utf-8

import sys
import re
import MySQLdb as mdb
from datetime import date, datetime
import os
import time

CONF_DIR = './'
REMOTE_PATHS = ['username1@remoteip1:remotepath1', 'username2@remoteip2:remotepath2']

today = str(date.today())
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class MySQL(object):
    def __init__(self, host='127.0.0.1', username='', password='', database=''):
        self.conn = mdb.connect(host, username, password, database)

    def closeLink(self):
        self.conn.close()


def remote_copy():
    conf_file_list = []
    import subprocess
    for remote_path in REMOTE_PATHS:
        remote_ip = remote_path.split('@')[1].split(':')[0]
        local_path = CONF_DIR + 'upstream_' + remote_ip + '.conf'
        cmd = "scp %s %s" %(remote_path, local_path)
        os.popen(cmd)
        conf_file_list.append(local_path)
    merge_files(conf_file_list)


def merge_files(file_list):
    '''
    当有多个upstream.conf来源时，在逐个远程复制后，将这些upstream配置文件
    合并成一个名为upstream_bak.conf的文件，用于后续处理
    '''
    result_files = CONF_DIR + 'upstream_bak.conf'
    with open(result_files, 'a') as t_fh:
        for file_path in file_list:
            with open(file_path, 'r') as s_fh:
                t_fh.write(s_fh.read())
                t_fh.write('\n')
            os.remove(file_path)


def insert_data():
    '''
    帮助函数：第一次将解析得到的数据插入数据库
    '''
    mysqlConnection = MySQL(username='dbadmin', password = 'dbadmin', database = 'dbadmin')
    conn = mysqlConnection.conn
    cursor = conn.cursor()

    data_list = parse_conf()
    data_to_insert = []
    for data_dict in data_list:
        data_to_insert.append((data_dict['upstream_name'], data_dict['server_ips'], data_dict['ip_count']))

    sql = "INSERT INTO upstream_data (upstream_name, upstream_ipList, upstream_ipCount) VALUES(%s, %s, %d)"
    cursor.executemany(sql, data_to_insert)
    conn.commit()
    cursor.close()
    mysqlConnection.closeLink()


def parse_conf():
    '''
    解析upstream配置文件
    '''
    conf_file_path = ''
    if len(sys.argv) > 1:
        conf_file_path = sys.argv[1]
    else:
        newfile_path = CONF_DIR + 'upstream_bak.conf'
        if os.path.exists(newfile_path) and os.path.isfile(newfile_path):
            conf_file_path = CONF_DIR + 'upstream_' + today + '.conf'
            os.rename(newfile_path, conf_file_path)

    if conf_file_path == '':
        sys.exit(1)

    section_pattern = r'(\s*upstream\s+([\w\.]+)\s?\n?{\n*(?:\s*.+?;(?:\s#\d*)?\n*)+})'
    section_obj = re.compile(section_pattern)

    server_pattern = r'\s*[\w\.\s#=:]+;'
    server_obj = re.compile(server_pattern)

    ip_pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?::\d+)?)'
    ip_obj = re.compile(ip_pattern)

    data_list = []
    content = ''
    with open(conf_file_path, 'r') as fh:
        for line in fh.readlines():
            line = line.strip()
            if not line.startswith('#'):
                content += line + "\n"

    section_list = section_obj.findall(content)
    for section in section_list:
        section_dict = {}
        upstream_name = section[1]
        servers = []
        upstream = section[0]
        server_list = server_obj.findall(upstream)
        for server in server_list:
            server = server.strip().strip("\n")
            if server.startswith("server"):
                server_ip = ip_obj.findall(server)[0]
                servers.append(server_ip)
        section_dict['upstream_name'] = upstream_name.strip()
        section_dict['server_ips'] = ';'.join(servers)
        section_dict['ip_count'] = str(len(servers))
        data_list.append(section_dict)
    return data_list


def update_data():
    '''
    将解析得到的新的upstream配置数据与数据库中的数据进行对比，看看是否有有效变更，
    然后对数据库做增删改
    '''
    mysqlConnection = MySQL(username='dbadmin', password = 'dbadmin', database = 'dbadmin')
    conn = mysqlConnection.conn
    cursor = conn.cursor()

    sql = "SELECT upstream_name, upstream_ipList FROM upstream_data"
    cursor.execute(sql)
    rows = cursor.fetchall()
    oldUpstreamData = {}
    for row in rows:
        oldUpstreamData[row[0]] = row[1].split(';')

    oldUpstreamNames = set(oldUpstreamData.keys())

    data_list = parse_conf()
    newUpstreamData = {}
    for data in data_list:
        newUpstreamData[data['upstream_name']] = data['server_ips'].split(';')

    newUpstreamNames = set(newUpstreamData.keys())

    '''
    每个upstream的变更状态：
        0表示未发生变更，
        1表示发生变更，
        2表示该upstream被删除
        3表示该upstream为新增
    '''
    dataWithStatus = []

    def compare_ip_list(upstream_name_set):
        for upstream_name in upstream_name_set:
            old_ip_set = set(oldUpstreamData[upstream_name])
            new_ip_set = set(newUpstreamData[upstream_name])
            if not (old_ip_set.issubset(new_ip_set) and old_ip_set.issuperset(new_ip_set)):
                dataWithStatus.append([upstream_name, list(new_ip_set), 1])
            else:
                dataWithStatus.append([upstream_name, list(old_ip_set), 0])

    sub = newUpstreamNames.issubset(oldUpstreamNames)
    sup = newUpstreamNames.issuperset(oldUpstreamNames)
    if sub and sup:
        compare_ip_list(oldUpstreamNames)
    else:
        upstreamToAdd = newUpstreamNames.difference(oldUpstreamNames)
        upstreamToDel = oldUpstreamNames.difference(newUpstreamNames)
        if len(upstreamToAdd) > 0:
            for upstream in upstreamToAdd:
                dataWithStatus.append([upstream, newUpstreamData[upstream], 3])
        if len(upstreamToDel) > 0:
            for upstream in upstreamToDel:
                dataWithStatus.append([upstream, oldUpstreamData[upstream], 2])
    print dataWithStatus
    flag = 0
    upstreamsToDel = []
    for data in dataWithStatus:
        sql = ''
        if data[2] == 0:
            sql = "UPDATE upstream_data SET upstream_status = %d WHERE upstream_name='%s'" % (0, data[0])
        elif data[2] == 1:
            flag += 1
            ip_list = ';'.join(data[1])
            sql = ("UPDATE upstream_data SET upstream_ipList='%s', upstream_ipCount=%d,"
                   "upstream_status=%d WHERE upstream_name='%s'" % (ip_list, len(data[1]), 1, data[0]))
        elif data[2] == 2:
            flag += 1
            sql = "DELETE FROM upstream_data WHERE upstream_name='%s'" % data[0]
            upstreamsToDel.append((data[0], ';'.join(data[1]), now))
        else:
            flag += 1
            sql = ("INSERT INTO upstream_data (upstream_name, upstream_ipList, upstream_ipCount, upstream_status) VALUES"
                   "('%s', '%s', %d, %d)" %(data[0], ';'.join(data[1]), len(data[1]), 3)
            )
        print sql
        cursor.execute(sql)

    if len(upstreamsToDel) > 0:
        cursor.executemany(
            "INSERT INTO upstream_deleted_data (upstream_name, upstream_ipList, date_toDelete) VALUES (%s, %s, %s)",
            upstreamsToDel
        )

    conn.commit()
    cursor.close()
    mysqlConnection.closeLink()

    # 若与数据库中的数据（即前一天的数据）对比，upstream配置文件未发生有效变化，则删除前一天的upstream配置文件
    if flag == 0:
        yesterday = date.fromtimestamp(time.time() - 3600 * 24)
        yesterday_filename = 'upstream_' + str(yesterday) + '.conf'
        path = CONF_DIR + yesterday_filename
        if os.path.exists(path) and os.path.isfile(path):
            os.remove(path)


if __name__ == '__main__':
    #remote_copy()
    #insert_data()
    #update_data()
    #parse_conf()
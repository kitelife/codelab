#!/usr/bin/env python
#coding: utf-8

import SocketServer
import subprocess


class task_request_handler(SocketServer.BaseRequestHandler):

    def __init__(self, request, client_address, server):
        SocketServer.BaseRequestHandler.__init__(self, request, client_address, server)

    def setup(self):
        return SocketServer.BaseRequestHandler.setup(self)

    def cmd_handler(self, cmd_part_list):
        result = ''
        try:
            child = subprocess.Popen(cmd_part_list, stdin=subprocess.PIPE, \
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            result = child.stdout.read()
        except Exception, e:
            exception_template = "{traceback}\n{strerror}"
            result = exception_template.format(traceback=e.child_traceback, strerror=e.strerror)
        return result

    def handle(self):
        bufsize = 1024
        data_part = self.request.recv(bufsize)
        data = data_part
        '''
        # 读取客户端发来的所有数据 
        while len(data_part) == bufsize:
            print '*'
            data_part = self.request.recv(bufsize)
            data += data_part
        '''
        data = data.split(' ')
        data_part_list = [element for element in data if element != '']
        print data_part_list
        result = self.cmd_handler(data_part_list)
        self.request.send(result)
        return

    def finish(self):
        return SocketServer.BaseRequestHandler.finish(self)


class server_daemon(SocketServer.TCPServer):

    def __init__(self, server_address, handler_class=task_request_handler):
        SocketServer.TCPServer.__init__(self, server_address, handler_class)
        return

    def server_activate(self):
        SocketServer.TCPServer.server_activate(self)
        return
     
    def serve_forever(self):
        while True:
            self.handle_request()
        return

    def handle_request(self):
        return SocketServer.TCPServer.handle_request(self)

    def verify_request(self, request, client_address):
        return SocketServer.TCPServer.verify_request(self, request, client_address)

    def process_request(self, request, client_address):
        return SocketServer.TCPServer.process_request(self, request, client_address)

    def server_close(self):
        return SocketServer.TCPServer.finish_request(self, request, client_address)

    def finish_request(self, request, client_address):
        return SocketServer.TCPServer.finish_request(self, request, client_address)

    def close_request(self, request_address):
        return SocketServer.TCPServer.close_request(self, request_address)


if __name__ == '__main__':
    import socket
    import threading

    address = ('localhost', 8080)
    server = server_daemon(address, task_request_handler)
    ip, port = server.server_address
    print ip, port

    server.serve_forever()

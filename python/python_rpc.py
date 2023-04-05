import functools
import json
from threading import Thread

import requests
from flask import Flask, request
from werkzeug.exceptions import abort

class RPCServer(Flask):
    def __init__(self, request_handler):
        super(RPCServer, self).__init__(__name__)
        self.request_handler = request_handler
        self.add_url_rule('/<method_name>', view_func=self.handle_request, methods=['POST'])

    def handle_request(self, method_name):
        method = getattr(self.request_handler, method_name, None)
        if not callable(method):
            return abort(404)
        params = json.loads(request.data)
        return json.dumps(method(*params['args'], **params['kwargs']))

class RPCClient(object):
    def __init__(self, host, port):
        self.base_url = 'http://{}:{}'.format(host, port)

    def __getattr__(self, method_name):
        return functools.partial(self.execute, method_name)

    def execute(self, method_name, *args, **kwargs):
        msg = json.dumps({'args':args, 'kwargs':kwargs})
        result = requests.post('{}/{}'.format(self.base_url, method_name), data=msg)
        if result.status_code == 200:
            return result.json()
        elif result.status_code == 404:
            raise Exception('Method not found: {}'.format(method_name))
        raise Exception('Unknown error')


class FooServer(object):
    def add(self, x, y):
        return x + y

    def mul(self, x, y):
        return x * y

rpc_server = RPCServer(FooServer())
server_thread = Thread(target=lambda: rpc_server.run(port=9901))
server_thread.daemon = True
server_thread.start()
foo = RPCClient(host='localhost', port=9901)
print foo.add(1,2), foo.mul(3, 4) # 3 12
print foo.div(1,2)

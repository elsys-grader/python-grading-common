import xmlrpc.client
import os
DEBUG_AUTH_TOKEN = '12345'

rpc = xmlrpc.client.ServerProxy('http://172.17.0.1:' + os.environ['PORT'])
token = os.environ.get('AUTH', DEBUG_AUTH_TOKEN)


def start_container():
    rpc.start_container(token)


def exec_step(command, decode='utf8'):
    rc, stdout, stderr, stdplex = rpc.exec_step(token, command)

    if decode is not None:
        return rc, stdout.data.decode(decode), stderr.data.decode(decode),\
               stdplex.data.decode(decode)
    return rc, stdout.data, stderr.data, stdplex.data

#!python
# https://github.com/takashiharano/envchk

import os
import sys
import socket
import datetime

info = ''

def get_env_info():
    now = datetime.datetime.now()
    #date_time = now.strftime('%Y-%m-%d %H:%M:%S.%f %z')
    date_time = now.strftime('%Y-%m-%d %H:%M:%S.%f') + ' +09:00'
    remote_addr = os.environ.get('REMOTE_ADDR', '')
    try:
        host_name = socket.gethostbyaddr(remote_addr)[0]
    except Exception as e:
        host_name = 'N/A'

    add_info('SYSTEM TIME      : ' + date_time)
    add_info('SERVER_NAME      : ' + os.environ.get('SERVER_NAME', ''))
    add_info('SERVER_ADDR      : ' + os.environ.get('SERVER_ADDR', ''))
    add_info('SERVER_PORT      : ' + os.environ.get('SERVER_PORT', ''))
    add_info('GATEWAY_INTERFACE: ' + os.environ.get('GATEWAY_INTERFACE', ''))
    add_info('SERVER_SOFTWARE  : ' + os.environ.get('SERVER_SOFTWARE', ''))
    add_info('')
    add_info('HOST ADDRESS     : ' + remote_addr)
    add_info('HOST NAME        : ' + host_name)
    add_info('REQUEST_METHOD   : ' + os.environ.get('REQUEST_METHOD', ''))
    add_info('REQUEST_URI      : ' + os.environ.get('REQUEST_URI', ''))
    add_info('SERVER_PROTOCOL  : ' + os.environ.get('SERVER_PROTOCOL', ''))
    add_info('QUERY_STRING     : ' + os.environ.get('QUERY_STRING', 'N/A'))
    add_info('REMOTE_USER      : ' + os.environ.get('REMOTE_USER', 'N/A'))
    add_info('REMOTE_PORT      : ' + os.environ.get('REMOTE_PORT', ''))
    add_info('Content-Length   : ' + os.environ.get('CONTENT_LENGTH', 'N/A'))
    add_info('Content-Type     : ' + os.environ.get('CONTENT_TYPE', 'N/A'))
    add_info('User-Agent       : ' + os.environ.get('HTTP_USER_AGENT', ''))
    add_info('Accept           : ' + os.environ.get('HTTP_ACCEPT', ''))
    add_info('Accept-Language  : ' + os.environ.get('HTTP_ACCEPT_LANGUAGE', 'N/A'))
    add_info('Accept-Charset   : ' + os.environ.get('HTTP_ACCEPT_CHARSET', 'N/A'))
    add_info('Accept-Encoding  : ' + os.environ.get('HTTP_ACCEPT_ENCODING', 'N/A'))
    add_info('Cookie           : ' + os.environ.get('HTTP_COOKIE', 'N/A'))
    add_info('Referer          : ' + os.environ.get('HTTP_REFERER', 'N/A'))
    add_info('Connection       : ' + os.environ.get('HTTP_CONNECTION', 'N/A'))
    add_info('Proxy-Connection : ' + os.environ.get('HTTP_PROXY_CONNECTION', 'N/A'))
    add_info('Via              : ' + os.environ.get('HTTP_VIA', 'N/A'))
    add_info('X-Forwarded-For  : ' + os.environ.get('HTTP_X_FORWARDED_FOR', 'N/A'))
    add_info('X-Forwarded-Host : ' + os.environ.get('HTTP_X_FORWARDED_HOST', 'N/A'))
    add_info('X-Forwarded-Proto: ' + os.environ.get('HTTP_X_FORWARDED_PROTO', 'N/A'))
    add_info('Upgrade-Insecure-Requests: ' + os.environ.get('HTTP_UPGRADE_INSECURE_REQUESTS', 'N/A'))
    add_info('')
    add_info('stdin: ' + sys.stdin.read())

def add_info(content):
    global info
    info += content + '\n'

def main():
    try:
        get_env_info()
        global info
        content = info
    except Exception as e:
        content = str(e)

    print('Content-Type: text/plain')
    print()
    print(content)

main()

#!/usr/bin/env python
# https://github.com/takashiharano/envchk

import os
import socket
import datetime

http_header = ''
http_body = ''

def get_env_info():
  now = datetime.datetime.now() 
  date_time = now.strftime('%Y-%m-%d %H:%M:%S.%f %z')
  remote_addr = os.environ.get('REMOTE_ADDR', '')
  try:
    host_name = socket.gethostbyaddr(remote_addr)[0]
  except Exception as e:
    host_name = 'N/A'

  add_http_header('Content-Type', 'text/plain')
  add_http_body('SYSTEM TIME      : ' + date_time)
  add_http_body('SERVER_NAME      : ' + os.environ.get('SERVER_NAME', ''))
  add_http_body('SERVER_PORT      : ' + os.environ.get('SERVER_PORT', ''))
  add_http_body('GATEWAY_INTERFACE: ' + os.environ.get('GATEWAY_INTERFACE', ''))
  add_http_body('SERVER_SOFTWARE  : ' + os.environ.get('SERVER_SOFTWARE', ''))
  add_http_body('')
  add_http_body('HOST ADDRESS     : ' + remote_addr)
  add_http_body('HOST NAME        : ' + host_name)
  add_http_body('REQUEST_METHOD   : ' + os.environ.get('REQUEST_METHOD', ''))
  add_http_body('REQUEST_URI      : ' + os.environ.get('REQUEST_URI', ''))
  add_http_body('SERVER_PROTOCOL  : ' + os.environ.get('SERVER_PROTOCOL', ''))
  add_http_body('QUERY_STRING     : ' + os.environ.get('QUERY_STRING', 'N/A'))
  add_http_body('REMOTE_USER      : ' + os.environ.get('REMOTE_USER', 'N/A'))
  add_http_body('REMOTE_PORT      : ' + os.environ.get('REMOTE_PORT', ''))
  add_http_body('Content-Length   : ' + os.environ.get('CONTENT_LENGTH', 'N/A'))
  add_http_body('Content-Type     : ' + os.environ.get('CONTENT_TYPE', 'N/A'))
  add_http_body('User-Agent       : ' + os.environ.get('HTTP_USER_AGENT', ''))
  add_http_body('Accept           : ' + os.environ.get('HTTP_ACCEPT', ''))
  add_http_body('Accept-Language  : ' + os.environ.get('HTTP_ACCEPT_LANGUAGE', 'N/A'))
  add_http_body('Accept-Charset   : ' + os.environ.get('HTTP_ACCEPT_CHARSET', 'N/A'))
  add_http_body('Accept-Encoding  : ' + os.environ.get('HTTP_ACCEPT_ENCODING', 'N/A'))
  add_http_body('Cookie           : ' + os.environ.get('HTTP_COOKIE', 'N/A'))
  add_http_body('Referer          : ' + os.environ.get('HTTP_REFERER', 'N/A'))
  add_http_body('Via              : ' + os.environ.get('HTTP_VIA', 'N/A'))
  add_http_body('Proxy-Connection : ' + os.environ.get('PROXY_CONNECTION', 'N/A'))

def add_http_header(key, val):
  global http_header
  http_header += key + ': ' + val + '\n'

def add_http_body(content):
  global http_body
  http_body += content + '\n'

def send_response(content):
  print(http_header)
  print(content)

def main():
  try:
    get_env_info()
    global http_body
    content = http_body
  except Exception as e:
    content = str(e)
  send_response(content)

main()

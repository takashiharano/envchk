#!/usr/bin/env python
# https://github.com/takashiharano/envchk

import os
import socket
import datetime

response_header = ''
response_body = ''

def get_env_info():
  now = datetime.datetime.now() 
  date_time = now.strftime('%Y-%m-%d %H:%M:%S.%f %z')
  remote_addr = os.environ.get('REMOTE_ADDR', '')
  try:
    host_name = socket.gethostbyaddr(remote_addr)[0]
  except Exception as e:
    host_name = 'N/A'

  add_body('SYSTEM TIME      : ' + date_time)
  add_body('SERVER_NAME      : ' + os.environ.get('SERVER_NAME', ''))
  add_body('SERVER_PORT      : ' + os.environ.get('SERVER_PORT', ''))
  add_body('GATEWAY_INTERFACE: ' + os.environ.get('GATEWAY_INTERFACE', ''))
  add_body('SERVER_SOFTWARE  : ' + os.environ.get('SERVER_SOFTWARE', ''))
  add_body('')
  add_body('HOST ADDRESS     : ' + remote_addr)
  add_body('HOST NAME        : ' + host_name)
  add_body('REQUEST_METHOD   : ' + os.environ.get('REQUEST_METHOD', ''))
  add_body('REQUEST_URI      : ' + os.environ.get('REQUEST_URI', ''))
  add_body('SERVER_PROTOCOL  : ' + os.environ.get('SERVER_PROTOCOL', ''))
  add_body('QUERY_STRING     : ' + os.environ.get('QUERY_STRING', 'N/A'))
  add_body('REMOTE_USER      : ' + os.environ.get('REMOTE_USER', 'N/A'))
  add_body('REMOTE_PORT      : ' + os.environ.get('REMOTE_PORT', ''))
  add_body('Content-Length   : ' + os.environ.get('CONTENT_LENGTH', 'N/A'))
  add_body('Content-Type     : ' + os.environ.get('CONTENT_TYPE', 'N/A'))
  add_body('User-Agent       : ' + os.environ.get('HTTP_USER_AGENT', ''))
  add_body('Accept           : ' + os.environ.get('HTTP_ACCEPT', ''))
  add_body('Accept-Language  : ' + os.environ.get('HTTP_ACCEPT_LANGUAGE', 'N/A'))
  add_body('Accept-Charset   : ' + os.environ.get('HTTP_ACCEPT_CHARSET', 'N/A'))
  add_body('Accept-Encoding  : ' + os.environ.get('HTTP_ACCEPT_ENCODING', 'N/A'))
  add_body('Cookie           : ' + os.environ.get('HTTP_COOKIE', 'N/A'))
  add_body('Referer          : ' + os.environ.get('HTTP_REFERER', 'N/A'))
  add_body('Via              : ' + os.environ.get('HTTP_VIA', 'N/A'))
  add_body('Proxy-Connection : ' + os.environ.get('PROXY_CONNECTION', 'N/A'))

def add_body(content):
  global response_body
  response_body += content + '\n'

def main():
  try:
    get_env_info()
    global response_body
    content = response_body
  except Exception as e:
    content = str(e)

  print('Content-Type: text/plain')
  print()
  print(content)

main()

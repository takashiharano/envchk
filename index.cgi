#!/usr/bin/python3
#!python
#==============================================================================
# envchk
# Copyright 2023 Takashi Harano
# Released under the MIT license
# https://github.com/takashiharano/envchk
# Created: 20230427
# Updated: 20230624
#==============================================================================

import sys
import os

ROOT_DIR = '../'
sys.path.append(os.path.join(os.path.dirname(__file__), ROOT_DIR + 'libs'))
import util

util.append_system_path(__file__, ROOT_DIR + 'websys/bin')
try:
    import web
except:
    pass

DATA_FILE_PATH =  './log.txt'
DATA_MAX_RECORDS = 1000
TZ_OFFSET = util.get_tz(True)

#------------------------------------------------------------------------------
def get_info():
    info = {}
    info['timestamp'] = util.get_timestamp()
    info['method'] = os.environ.get('REQUEST_METHOD', '')
    info['addr'] = os.environ.get('REMOTE_ADDR', '')
    info['host']= util.get_host_name(info['addr'])
    info['ua'] = os.environ.get('HTTP_USER_AGENT', '')
    info['accept'] = os.environ.get('HTTP_ACCEPT', '')
    info['accept_lang'] = os.environ.get('HTTP_ACCEPT_LANGUAGE', '')
    info['accept_charset'] = os.environ.get('HTTP_ACCEPT_CHARSET', '')
    info['accept_encoding'] = os.environ.get('HTTP_ACCEPT_ENCODING', '')
    info['request_uri'] = os.environ.get('REQUEST_URI', '')
    info['referer'] = os.environ.get('HTTP_REFERER', '')
    info['remote_port'] = os.environ.get('REMOTE_PORT', '')
    info['remote_user'] = os.environ.get('REMOTE_USER', '')
    info['connection'] = os.environ.get('HTTP_CONNECTION', '')
    info['proxy_connection'] = os.environ.get('HTTP_PROXY_CONNECTION', '')
    info['via'] = os.environ.get('HTTP_VIA', '')
    info['x_forwarded_for'] = os.environ.get('HTTP_X_FORWARDED_FOR', '')
    info['x_forwarded_host'] = os.environ.get('HTTP_X_FORWARDED_HOST', '')
    info['x_forwarded_proto'] = os.environ.get('HTTP_X_FORWARDED_PROTO', '')
    info['sv_protocol'] = os.environ.get('SERVER_PROTOCOL', '')
    info['upgrade_insecure_requests'] = os.environ.get('HTTP_UPGRADE_INSECURE_REQUESTS', '')
    info['cookie'] = os.environ.get('HTTP_COOKIE', '')
    info['query_string'] = os.environ.get('QUERY_STRING', '')
    info['content_type'] = os.environ.get('CONTENT_TYPE', '')
    info['content_length'] = os.environ.get('CONTENT_LENGTH', '')
    info['stdin'] = util.read_stdin()
    return info

#------------------------------------------------------------------------------
def save_log(info):
    dat = util.to_json(info)
    path = DATA_FILE_PATH
    util.append_line_to_text_file(path, dat, max=DATA_MAX_RECORDS)

#------------------------------------------------------------------------------
def view():
    log_list = util.read_text_file_as_list(DATA_FILE_PATH)
    log_list.reverse()

    html = '''<!DOCTYPE html>
<html>
<head>
<meta http-equiv="X-UA-Compatible" content="IE=Edge">
<meta charset="utf-8">
<title>Test Log</title>
<style>
body {
  background: #000;
  color: #fff;
  font-size: 12px;
  font-family: Consolas;
}
table {
  width: 100%;
  border: 1px solid #06a;
  margin-bottom: 8px;
  border-collapse: collapse;
  background:linear-gradient(#000070, #000010);
}
pre {
  margin: 0;
  font-family: Consolas;
}
.nodata {
  color: #777;
}
.pale {
  opacity: 0.65;
}
</style>
</head>
<body>
'''
    html += ''
    html += '<div style="text-align:center;">'
    html += '<div style="width:900px;margin:auto;text-align:left;">'
    html += util.DateTime().to_str(fmt='%Y-%m-%d %W %H:%M:%S.%f') + ' ' + TZ_OFFSET
    html += '<br><br>'

    list_size = len(log_list)
    for i in range(list_size):
        record = log_list[i]

        info = util.from_json(record)

        timestamp = info['timestamp']
        dt = util.DateTime(timestamp).to_str(fmt='%Y-%m-%d %W %H:%M:%S.%f')
        dt = util.replace(dt, 'SUN', '<span style="color:#fa8;">SUN</span>')
        dt = util.replace(dt, 'MON', '<span style="color:#ffc;">MON</span>')
        dt = util.replace(dt, 'TUE', '<span style="color:#f84;">TUE</span>')
        dt = util.replace(dt, 'WED', '<span style="color:#8df;">WED</span>')
        dt = util.replace(dt, 'THU', '<span style="color:#db6;">THU</span>')
        dt = util.replace(dt, 'FRI', '<span style="color:#ff8;">FRI</span>')
        dt = util.replace(dt, 'SAT', '<span style="color:#afe;">SAT</span>')

        index = list_size - i
        dat = '[' + str(index) + '] '
        dat += dt
        dat += ' ' + TZ_OFFSET
        dat += ' (' + str(timestamp) + ')'
        dat += '\n'
        dat += build_data_string(info, True)

        html += '<table>'
        html += '<tr>'
        html += '<td><pre>' + dat + '</pre></td>'
        html += '</tr>'
        html += '</table>'

    html += '</div>'
    html += '''
</body>
</html>'''
    util.send_response(html, 'text/html')

def conv_nodata_if_unavailable(s):
    if s == '':
        s = '<span class="nodata">N/A</span>'
    return s

def build_data_string(info, for_html=False):
    s = ''
    s += build_field_string(info, 'METHOD           ', 'method', for_html) + '\n'
    s += build_field_string(info, 'ADDR             ', 'addr', for_html) + '\n'
    s += build_field_string(info, 'HOST             ', 'host', for_html) + '\n'
    s += build_field_string(info, 'User-Agent       ', 'ua', for_html) + '\n'
    s += build_field_string(info, 'Accept           ', 'accept', for_html) + '\n'
    s += build_field_string(info, 'Accept-Language  ', 'accept_lang', for_html) + '\n'
    s += build_field_string(info, 'Accept-Encoding  ', 'accept_encoding', for_html) + '\n'
    s += build_field_string(info, 'Accept-Charset   ', 'accept_charset', for_html) + '\n'
    s += build_field_string(info, 'REQUEST_URI      ', 'request_uri', for_html) + '\n'
    s += build_field_string(info, 'HTTP_REFERER     ', 'referer', for_html) + '\n'
    s += build_field_string(info, 'REMOTE_PORT      ', 'remote_port', for_html) + '\n'
    s += build_field_string(info, 'REMOTE_USER      ', 'remote_user', for_html) + '\n'
    s += build_field_string(info, 'Connection       ', 'connection', for_html) + '\n'
    s += build_field_string(info, 'Proxy-Connection ', 'proxy_connection', for_html) + '\n'
    s += build_field_string(info, 'Via              ', 'via', for_html) + '\n'
    s += build_field_string(info, 'X-Forwarded-For  ', 'x_forwarded_for', for_html) + '\n' 
    s += build_field_string(info, 'X-Forwarded-Host ', 'x_forwarded_host', for_html) + '\n'
    s += build_field_string(info, 'X-Forwarded-Proto', 'x_forwarded_proto', for_html) + '\n'
    s += build_field_string(info, 'SERVER_PROTOCOL  ', 'sv_protocol', for_html) + '\n'
    s += build_field_string(info, 'Upgrade-Insecure-Requests', 'upgrade_insecure_requests', for_html) + '\n'
    s += build_field_string(info, 'Cookie           ', 'cookie', for_html) + '\n'
    s += build_field_string(info, 'QUERY_STRING     ', 'query_string', for_html) + '\n'
    s += build_field_string(info, 'Content-Type     ', 'content_type', for_html) + '\n'
    s += build_field_string(info, 'Content-Length   ', 'content_length', for_html) + '\n'
    s += build_field_string(info, 'stdin            ', 'stdin', for_html)
    return s

def build_field_string(info, name, key, for_html):
    v = ''
    if key in info:
        v = info[key]

    if for_html:
        v = conv_nodata_if_unavailable(v)

    s = name + ': ' + v
    return s

def send_result(info):
    timestamp = info['timestamp']
    date_time = util.DateTime(timestamp).to_str(fmt='%Y-%m-%d %W %H:%M:%S.%f')
    date_time += ' ' + TZ_OFFSET
    s = 'SYSTEM_TIME      : ' + date_time + ' (' + str(timestamp) + ')\n'
    s += build_data_string(info)
    util.send_response(s)

#------------------------------------------------------------------------------
# curl http://localhost/test/
# curl -X POST -d "abc=123" http://localhost/test/
# curl -I http://localhost/test/
# curl -H "Authorization: Basic <id:pw in BASE64>" http://localhost/401/
# curl -H "Cookie: sid=12345678" http://localhost/test/
def main():
    q = util.get_query()
    if q == 'view':
        if 'web' in sys.modules:
            context = web.on_access()
            if context.is_authorized():
                view()
                return

    info = get_info()
    save_log(info)

    if q == 'ip':
        util.send_response(info['addr'] + '\n')
    if q == 'host':
        util.send_response(info['host'] + '\n')
    else:
        send_result(info)

main()

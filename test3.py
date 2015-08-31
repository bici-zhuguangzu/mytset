#!/usr/bin/python
#coding=utf-8

import urllib
import urllib2
import simplejson as json
username="Admin"
passwd="123qwe"

def post(url, data):
    req = urllib2.Request(url, data)
    print req       # 生成页面请求的完整数据
    response = urllib2.urlopen(req)       # 发送页面请求
    return response.read()

def main():
    posturl = "http://192.168.12.210/zabbix/api_jsonrpc.php"
    dd = { "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
    "user": username,
    "password": "123qwe"
    },
    "id": 1, 
    "auth": None
    }
    data=json.dumps(dd)
    print type(data)
    print post(posturl, data)

if __name__ == '__main__':
    main() 
#!/usr/bin/python
#coding=utf-8

import urllib
import urllib2
import simplejson as json
username="Admin"
passwd="123qwe"

def post(url, data):
    req = urllib2.Request(url, data)
    req.add_header('Content-type', 'application/json')       # 发送页面请求
    response = urllib2.urlopen(req)
    resp = response.read()
    ss=json.loads(resp)
    token=ss["result"]
    return token

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
    print post(posturl, data)
    

if __name__ == '__main__':
    main() 
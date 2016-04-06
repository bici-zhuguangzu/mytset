#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-04-05 08:23:50
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

from urllib2 import Request, urlopen, HTTPError, URLError
from urllib import urlencode


class urltest:
    """docstring for urltest"""

    def __init__(self, arg, arg1):
        self.url = arg
        self.value = arg1

    def makedata(self):
        data = urlencode(self.value)
        return data

    def acc_url(self, data):
        req = Request(self.url)
        try:
            respone = urlopen(req, data)
        except HTTPError, e:
            print e.code
        except URLError, e:
            print e.reason
        else:
            print respone.read()


values = {'username': 'guangzu', 'passwd': '123456'}
url = 'http://www.baidu.com'
test = urltest(url, values)
data = test.makedata()
print data
for i in xrange(1,100):
    print test.acc_url(data)

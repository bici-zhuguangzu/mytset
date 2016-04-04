#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-04-04 23:35:51
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     : class test
# @Version : $Id$


import os


class test():
    """docstring for test"""

    def __init__(self, arg):
        self.command = arg

    def list(self):
        print self.command
        list = (os.popen(self.command).readline())
        return list

    def list1(self):
        list = [os.popen(self.command).readline()]
        return list

m = test('ls')
print type(m.list())

print type(m.list1())


print m.list()
print m.list1()

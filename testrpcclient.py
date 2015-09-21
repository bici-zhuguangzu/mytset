#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-21 11:07:37
# @Author  : guangzu (guangzu_zhu@163.com)
# @Link    : blog.zhuguangzu.xyz
# @Version : $Id$

from xmlrpclib import ServerProxy

s = ServerProxy("http://127.0.0.1:8787")


def diaoyong():
    print s.testprint("rpc test")

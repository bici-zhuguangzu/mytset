#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-21 11:02:37
# @Author  : guangzu (guangzu_zhu@163.com)
# @Link    : blog.zhuguangzu.xyz
# @Version : $Id$

from SimpleXMLRPCServer import SimpleXMLRPCServer
import testqrcode


def testprint(test):
    return "this is a %s" %test


def startservice():
    s = SimpleXMLRPCServer(('127.0.0.1', 8787))
    s.register_function(testprint)
    s.serve_forever()


def main():
    startservice()


if __name__ == '__main__':
    main()

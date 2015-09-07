#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-07 15:24:47
# @Author  : guangzu (guangzu_zhu@163.com)
# @Link    : blog.zhuguangzu.xyz
# @Version : $Id$

import XlsxRead
import deploy
import threading
import time

FileName = "/Users/zhuguangzu1/Documents/2.xlsx"


def printtest(test):
    print test
    time.sleep(1)


def deployfromxlsx():
    HostDict = XlsxRead.MakeDict(FileName)
    del HostDict[u'名称']
    for key in HostDict.keys():
        ips = key
        hostname = HostDict[key]
        test = ips + ":" + hostname
        # target可以更换为deploys，args为ips hostname
        t1 = threading.Thread(target=printtest, args=(test,))
        t1.start()
        # deploy.deploys(ips, hostname)


def main():
    deployfromxlsx()


if __name__ == '__main__':
    main()

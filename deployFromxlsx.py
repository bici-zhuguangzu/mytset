#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-07 15:24:47
# @Author  : guangzu (guangzu_zhu@163.com)
# @Link    : blog.zhuguangzu.xyz
# @Version : $Id$

import XlsxRead
from deploy import deploys
import multiprocessing
import time

FileName = "/Users/zhuguangzu1/Documents/2.xlsx"


def printtest(test):
    print test
    time.sleep(1)


def deploywithinput():
    hostname = raw_input("enter hostname:")
    ips = raw_input("enter ip:")
    print hostname + ":" + ips


def deployfromxlsx():
    count = XlsxRead.CountOfDict()
    HostDict = XlsxRead.MakeDict(FileName)
    pool = multiprocessing.Pool(processes=count)
    for key in HostDict.keys():
        hostname = key
        ips = HostDict[key]
        test = hostname + ":" + ips
        pool.apply_async(printtest, (test, ))  # 可以更改deploys
    pool.close()
    pool.join()


def main():
    deployfromxlsx()


if __name__ == '__main__':
    main()

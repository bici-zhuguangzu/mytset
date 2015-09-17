#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-17 14:08:02
# @Author  : guangzu (guangzu_zhu@163.com)
# @Link    : blog.zhuguangzu.xyz
# @Version : $Id$

import pycurl
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d]  \
                    %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='executeResult.log',
                    filemode='a')  # 指定日志记录方式为追加


def testcurl(url):
    curl = pycurl.Curl()
    curl.setopt(pycurl.URL, url)
    curl.setopt(pycurl.CONNECTTIMEOUT, 10)
    curl.perform()
    return curl.getinfo(curl.HTTP_CODE)  # 返回http code
    curl.close


def main():
    url = '192.168.12.210'
    if testcurl(url) != 200:
        logging.warning("execute failure")
    else:
        logging.debug("execute ok")


if __name__ == '__main__':
    main()

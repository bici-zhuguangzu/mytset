#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-17 14:08:02
# @Author  : guangzu (guangzu_zhu@163.com)
# @Link    : blog.zhuguangzu.xyz
# @Version : $Id$

import pycurl
import logging
import StringIO


url = "192.168.12.210"


def curlUrl(url):
    curl = pycurl.Curl()
    output = StringIO.StringIO()
    curl.setopt(pycurl.URL, url)
    curl.setopt(pycurl.CONNECTTIMEOUT, 10)
    # 把StringIO的写函数注册到pycurl的WRITEFUNCTION中，即pycurl所有获取的内容都写入到StringIO中，如果没有这一句，pycurl就会把所有的内容在默认的输出器中输出
    curl.setopt(pycurl.WRITEFUNCTION, output.write)
    curl.perform()
    # output.getvalue()
    return curl.getinfo(curl.HTTP_CODE)  # 返回http code
    curl.close
    output.close


def accesslog():
    retrunCode = curlUrl(url)
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d]  \
                    %(levelname)s %(message)s',
                        datefmt='%a, %Y-%m-%d %H:%M:%S',
                        filename='../logs/executeResult.log',
                        filemode='a')  # 指定日志记录方式为追加

    if retrunCode != 200:
        logging.warning("access failure with HTTP_CODE %s" % retrunCode)
    else:
        logging.debug("access ok %s" % retrunCode)


def main():
    accesslog()


if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-17 14:47:11
# @Author  : guangzu (guangzu_zhu@163.com)
# @Link    : blog.zhuguangzu.xyz
# @Version : $Id$


import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d]  \
                    %(levelname)s %(message)s',
                    datefmt='%a, %d-%m-%Y %H:%M:%S',
                    filename='myapp.log',
                    filemode='a')    # 指定日志为追加模式

##########################################################################
# 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
##########################################################################

logging.debug('This is debug message')
logging.info('This is info message111')
logging.warning('This is warning message')

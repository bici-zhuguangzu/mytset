#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-11 10:07:48
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

from enum import Enum

class testmeiju(Enum):
    """docstring for testmeiju"""
    a = 1
    b = 2
    c = 3

if __name__ == '__main__':
    a= testmeiju
    for data in a:
        print(data.value)
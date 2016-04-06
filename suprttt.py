#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-04-06 17:06:47
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

import os


class supertst:
    """docstring for supertst"""

    def __init__(self, arg):
        self.data = arg

    def printdata(self):
        print self.data


class tt(supertst):
    """docstring for tt"""

    def __init__(self, arg, arg1):
        supertst.__init__(self, arg)
        self.value = arg1

    def printvalue(self):
        print self.value


m = tt('you', 'self')
m.printdata()
m.printvalue()

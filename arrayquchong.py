#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-04-24 13:33:17
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

import os


class quchong(object):
    """docstring for quchonng"""

    def __init__(self, *arg):
        super(quchong, self).__init__()
        self.arg = arg
        self.list = list(self.arg)

    def funcqc(self):
        yuanshi = list(self.arg)
        chuli = set(yuanshi)
        if chuli is None:
            os._exit()
        else:
            for i in chuli:
                yuanshi.remove(i)
            yuanshi = set(yuanshi)
            return yuanshi

    def countnum(self):
        listchongfu = self.funcqc()
        yuanshi = list(self.arg)
        for i in listchongfu:
            count = yuanshi.count(i)
            print i, count


if __name__ == '__main__':
    action = quchong('1', '2', '2', '2', '3', '1', '4', '4')
    print action.funcqc()
    print action.countnum()

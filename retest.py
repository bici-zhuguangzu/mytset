#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-04-23 10:29:51
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

import re


class testre(object):
    """docstring for testre"""

    def __init__(self, filename):
        self.filename = filename

    def lvsre(self):
        matchcontent = ['12', '34', '45']
        print type(matchcontent)
        with open(self.filename, 'r') as f:
            contenet = f.readlines()
            f.close
        print type(contenet)
        for linecontent in contenet:
            for i in matchcontent:
                lvsmatech = re.compile(i)
                matchtrue = lvsmatech.search(linecontent)
                if matchtrue is not None:
                    print linecontent

if __name__ == '__main__':
    test = testre('testfile')
    test.lvsre()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-04-06 17:06:47
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

import os


class A(object):

    def __init__(self):
        print "A"
        super(A, self).__init__()

    def p(self):
        print "AA"


class B(object):

    def __init__(self):
        print "B"
        super(B, self).__init__()

    def p(self):
        print "BB"


class C(A, B):

    def __init__(self):
        print "C"
        A.__init__(self)
        B.__init__(self)

    def p(self):
        print "CC"
        A.p(self)
        B.p(self)

if __name__ == '__main__':
    c = C()
    c.p()

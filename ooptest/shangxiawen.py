#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-21 10:35:21
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

from contextlib import contextmanager


@contextmanager
def open_file(name):
    f = open(name, 'w')
    yield f
    f.close()

if __name__ == '__main__':
    with open_file('guangau') as f:
        f.write('123')

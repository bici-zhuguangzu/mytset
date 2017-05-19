#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-27 07:30:03
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

def test():
    s = -1
    for i in range(10):
        s += 1
        yield i,s

if __name__ == '__main__':
    d = test()
    for data in d:
        print(data)

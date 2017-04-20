#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-12 14:37:10
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$


def test(a='1'):
    print(a)




def test1(x):
    for i in x:
        if isinstance(i,list):
            test1(i)
        else:
            print(i)

if __name__ == '__main__':
    test1([['1'],['2']])


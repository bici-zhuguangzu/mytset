#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-30 19:07:47
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# @Version : $Id$

import os


def test():
    message = os.popen('ls -al')
    return message.read()


if __name__ == '__main__':
    print test()

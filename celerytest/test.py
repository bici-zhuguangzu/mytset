#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-29 23:08:37
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

import os
from tasks import add
if __name__ == '__main__':
    for i in range(100):
        for j in range(100):
            add.delay(i, j)
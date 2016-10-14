#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-14 22:13:18
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os

'''
测试unicode
'''

s = "你是我的眼"

asarray = s.split('的')
print(asarray[0])


'''
测试os.scandir
'''
f = os.scandir('.')
for dir in f:
    print(dir)

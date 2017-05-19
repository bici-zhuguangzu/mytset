#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-25 17:34:08
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

import timeit

t = timeit.Timer("'{} {} {}'.format('1','2','3')")
t1 = timeit.Timer("' '.join(['1','2','3'])")

print(t.timeit(1000000))
print(t1.timeit(1000000))

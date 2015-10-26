#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-25 22:44:02
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# @Version : $Id$


import rpyc

c = rpyc.connect('localhost', 12233)
print c.root.sum(1, 2)
c.close()

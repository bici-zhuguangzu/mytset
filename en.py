#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-26 17:40:47
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$
from enum import Enum


a = ['q','w','e','r','v']

d= {a.index(i):i for i in a}

print(d)


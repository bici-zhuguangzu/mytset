#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-29 23:05:05
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

import celery

@celery.task
def add(x, y):  
    z = x+y
    return z 

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-29 23:07:51
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

BROKER_URL = "redis://192.168.10.117:6379/0"

CELERY_IMPORTS = ("tasks.add", )

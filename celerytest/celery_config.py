#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-30 10:01:11
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$



from celery import Celery

app = Celery('celery_config', broker='redis://192.168.10.117:6379/0', include=['celery_blog'])

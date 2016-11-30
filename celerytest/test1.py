#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-30 10:09:43
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

from celery_blog import func

if __name__ == '__main__':
    func(['http://www.baidu.com', 'http://www.youku.com', 'http://www.sohu.com', 'http://www.sina.com.cn'])

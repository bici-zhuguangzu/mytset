#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-25 21:33:26
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# @Version : $Id$


hosts = ['192.168.10.191', '192.168.10.138', '192.168.10.164']
username = 'root'
passwd = '111111'
groups = {
    'webserver': ['192.168.10.191', '192.168.10.164'],
    'dbserver': ['192.168.10.138']
}

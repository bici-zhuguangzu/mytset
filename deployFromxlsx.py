#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-07 15:24:47
# @Author  : guangzu (guangzu_zhu@163.com)
# @Link    : blog.zhuguangzu.xyz
# @Version : $Id$

import XlsxRead
import deploy

FileName = "/Users/zhuguangzu1/Documents/2.xlsx"

HostDict = XlsxRead.MakeDict(FileName)
del HostDict[u'名称']
for key in HostDict.keys():
    ips = key
    hostname = HostDict[key]
    print ips + ":" + hostname
    deploy.deploys(ips, hostname)

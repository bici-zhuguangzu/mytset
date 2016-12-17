#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-21 15:01:41
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

import requests
import sys

DpoolURL =  'http://int.dpool.sina.com.cn/iplookup/iplookup.php?formart=js&ip='


class geip(object):
    """docstring for geip"""
    __slots__ = ('ip')
    def __init__(self):
        super(geip, self).__init__()
        
    def GetlocationForIp(self):
        FullUrl = DpoolURL + self.ip 
        return requests.get(FullUrl).text

    @property
    def location(self):
        return self.GetlocationForIp()[7:].lstrip()

if __name__ == '__main__':
    iplist = sys.argv[1:]
    for ip in iplist:
        f = geip()
        f.ip = ip
        print(f.location)
    
    

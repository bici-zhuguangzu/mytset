#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-25 11:44:43
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

import re
import os


class Praseconf(object):
    """docstring for Praseconf"""

    def __init__(self, filename):
        super(Praseconf, self).__init__()
        self.filename = filename

    def splitfiletoserver(self):
        serverlist = []
        with open(self.filename) as f:
            lines = f.read().split('server {')
            for line in lines:
                serverlist.append(line)
        return serverlist

    def getserverdict(self, lines):
        ip = ''
        cert = ''
        proxy_ip = ''
        line = lines.split('\n')
        for conf in line:
            confline = conf.lstrip()
            if re.search('\:443\;', confline):
                ip = confline.split(' ')[-1].split(':')[0]
            if re.search('ssl_certificate_key', confline):
                cert = confline.split(' ')[-1].split('/')[-2]
            if re.search('proxy_pass', confline):
                proxy_ip = confline.split(' ')[-1].split('//')[-1].strip(';')
        # print(ip, cert, proxy_ip)
        sigledict = ip
        sigledict = {}
        sigledict['vip'] = ip
        sigledict['cert'] = cert
        sigledict['proxy_ip'] = proxy_ip
        # print(sigledict)
        return sigledict

    def parserserverdict(self):
        conflist = []
        lines = self.splitfiletoserver()[2:-1]
        for line in lines:
            # print(line)
            confdict = self.getserverdict(line)
            conflist.append(confdict)
        print(conflist)
        # for line in lines:
        #     print(line)
        #     self.getserverdict(line)
        # for conf in serverconf:
        #     print(conf.lstrip())

if __name__ == '__main__':
    test = Praseconf('nginx-dx.conf')
    test.parserserverdict()

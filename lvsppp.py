#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-04-07 11:24:34
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

import re
import sys


class lvsprase:
    """docstring for lvsprase"""

    def __init__(self, filename):
        self.filename = filename

    def getfilelist(self):
        with open(self.filename) as f:
            line = f.read()
        f.close
        filemeta = re.split('\n|{|}|^$', line)
        return filemeta

    def rmzhushi(self):
        content = []
        filemeta = self.getfilelist()
        for x in filemeta:
            m = re.search('#', x)
            if m is None:
                content.append(x)
                content.append('\n')
        return content

    def getvip(self):
        lvsdict = self.getlvsdict()
        vip = lvsdict.keys()
        # print vip
        return vip

    def getlvsdict(self):
        group = []
        grouplist = []
        rsdict = {}
        filemeta = self.rmzhushi()
        for x in filemeta:
            group.append(x.strip())
        for x in group:
            m = re.search('virtual_server', x)
            n = re.search('real_server', x)
            p = re.search('weight', x)
            if m is not None:
                x = re.sub('virtual_server ', '\n', x)
                grouplist.append(x)
            if n is not None:
                x = re.sub('real_server ', 'flag', x)
                grouplist.append(x)
            if p is not None:
                x = re.sub('weight', '', x)
                grouplist.append(x)
        ss = ''.join(grouplist).split('\n')
        for x in ss:
            cfgstr = re.sub(' ', ',', x).split('flag')  # .remove('')
            # print len(cfgstr)
            if len(cfgstr) is not 1:
                key = cfgstr[0]
                value = cfgstr[1:]
                rsdict[key] = value
        return rsdict

    def welcomepage(self):
        print "this not bulid"

    def searchvip(self):
        lvsdict = self.getlvsdict()
        #print lvsdict
        vip = raw_input("pls input vip,port or quit: ")
        if vip in lvsdict.keys():
            print vip
            print 'rs    port    weight'
            rslist = lvsdict[vip]
            for x in rslist:
                print x
            self.searchvip()
        elif vip == 'quit':
            self.welcomepage()
        else:
            print 'error'
            self.searchvip()


if __name__ == '__main__':
    test = lvsprase('lvs.conf')
    # vip = test.getvip()
    # print vip
    # print test.getlvsdict()
    test.searchvip()

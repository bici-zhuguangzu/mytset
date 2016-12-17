#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-25 16:48:59
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

import re


class parselvsandvip(object):
    """docstring for parselvsvip"""

    def __init__(self, vipfilename, lvsfilename=''):
        super(parselvsandvip, self).__init__()
        self.vipconf = vipfilename
        self.lvsconf = lvsfilename

    def getallvip(self):
        vip_re_filter = r'\d+.\d+.\d+.\d+\/\d+'
        vipfilename = self.vipconf
        viplist = []
        with open(vipfilename, encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                if re.search(vip_re_filter, line):
                    vip = line.lstrip().split('/')[0]
                    if re.search('#', vip):
                        continue
                    else:
                        viplist.append(vip)
        # print(viplist)
        return viplist

    def getallvipwithvport(self):
        lvs_re_filter = 'virtual_server'
        vipwithvportlist = []
        lvsfilename = self.lvsconf
        with open(lvsfilename, encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                if re.search(lvs_re_filter, line):
                    vip = line.split(' ')[1]
                    vipwithvportlist.append(vip)
        # print(vipwithvportlist)
        return vipwithvportlist

    def getallgatewayip(self):
        allvip = self.getallvip()
        allvipwithvport = self.getallvipwithvport()
        snatip = list(set(allvip).difference(set(allvipwithvport)))
        # print(snatip)
        return snatip


if __name__ == '__main__':
    test = parselvsandvip('vip_cfg', 'lvs_cfg')
    # test.getallvip()
    # test.getallvipwithvport()
    test.getallgatewayip()

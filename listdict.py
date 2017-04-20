#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-19 17:33:21
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

vip_ext_option = [ { "delay_loop" : "15" }, { "lb_algo" : "wrr" }, { "lb_kind" : "DR" }, { "protocol" : "TCP" } ]

d = { "delay_loop" : "15" }

g = lambda x: x.keys()[0]
print(g(d))
items = [g(i) for i in vip_ext_option]
print(items)
if 'lb_algo' in items:
    print('ok')

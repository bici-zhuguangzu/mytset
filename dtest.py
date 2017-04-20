#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-14 11:17:25
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

_dict={'b':1,'f':7,'k':5,'s':8,'o':6,'a':3}

new = {v:k for k,v in _dict.items()}
print(new)
lst = sorted(_dict.values())
print(lst)
d= [new[k] for k in lst]
print(d)



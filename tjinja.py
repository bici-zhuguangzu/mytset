#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-04-08 13:19:35
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

from jinja2 import Template

template = Template('hello {{ name }}\nthis is a huanhang!')
template1 = Template('are you {{ name }}?')
print template.render(name ='john')
print template1.render(name = 'tom')

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-25 16:41:26
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$


from collections import Counter
import re
a = 'qw eer t'
x = re.sub(' ','',a)
v = (Counter(x))
print(v)
for k,v in  v.items():
    print(v)




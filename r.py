#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-16 16:38:52
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

import requests
import json


data = {"a":"we"}
data1 = json.dumps(data)
with requests.Session() as f:
    t = f.post("http://httpbin.org/post", json=data)
    print(f.__dict__)
    print(t.__dict__)
    print(t.ok)


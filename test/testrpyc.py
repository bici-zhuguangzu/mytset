#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-25 22:43:08
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# @Version : $Id$

import time
from rpyc import Service
from rpyc.utils.server import ThreadedServer


class TimeService(Service):

    def exposed_sum(self, a, b):
        return a + b

s = ThreadedServer(TimeService, port=12233, auto_register=False)
s.start()

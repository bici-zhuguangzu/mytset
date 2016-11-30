#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-27 11:18:01
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os


g =lambda x: x>5
s = lambda x: x*x

print(list(filter(g, range(10))))
print(list(map(s, range(10))))
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-21 11:35:44
# @Author  : guangzu (guangzu_zhu@163.com)
# @Link    : blog.zhuguangzu.xyz
# @Version : $Id$

from jsonrpc2 import JsonRpc
rpc = JsonRpc()


def testrpc(test1):
    return "this is a %s" % test1


def testrpc1(test1):
    return type(testrpc(test1))


rpc['testrpc'] = testrpc
rpc['testrpc1'] = testrpc1
rpc.
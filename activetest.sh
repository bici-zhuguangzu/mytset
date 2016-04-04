#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# DESC     :
# @Date    : 2015-12-09 11:04:44
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# @Version : $Id$

ping -c 2 -W 10 192.168.10.2
if [[ $? != 0 ]]; then
    ip=192.168.10.1
else
    ip=192.168.10.2
fi

echo $ip
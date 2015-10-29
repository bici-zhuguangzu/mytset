#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-28 16:51:51
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

from fabric.api import *
from fabric.colors import *
# from fabric.contrib.console import confirm
import config


env.hosts = config.hosts
env.user = config.username
env.password = config.passwd
env.roledefs = config.saltgroups


@roles('master')
def saltmaster():
    put
    run('./InstallSalt.sh master')


@roles('minion')
def saltminion():
    put
    run('./InstallSalt.sh minion')


@task
def saltInstall():
    execute(saltmaster)
    execute(saltminion)

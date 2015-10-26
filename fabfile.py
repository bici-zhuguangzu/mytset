#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-24 11:26:01
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# @Version : $Id$

from fabric.api import *
from fabric.colors import *
# from fabric.contrib.console import confirm
import config


env.hosts = config.hosts
env.user = config.username
env.password = config.passwd
env.roledefs = config.groups


@runs_once
@roles('webserver')
def webtask():
    print yellow('install nginx')
    with settings(warn_only=True):
        run('yum install nginx')


@runs_once
@roles('dbserver')
def dbtask():
    print yellow('install mysql')
    with settings(warn_only=True):
        run('yum install mysql-server')


@task
def deploy():
    execute(webtask)
    execute(dbtask)

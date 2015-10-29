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


@roles('webserver')
@parallel(pool_size=5)
def webtask():
    print yellow('install nginx')
    with settings(warn_only=True):
        # run('yum -y install nginx')
        run('yum -y install salt-minion')


@task
@roles('webserver')
def webstart():
    print yellow('start nginx')
    with settings(warn_only=True):
        run('service nginx restart')


@roles('dbserver')
def dbtask():
    print yellow('install mysql')
    with settings(warn_only=True):
        # run('yum -y install mysql-server')
        # run('service mysqld start')
        run('yum -y install salt-master')


@task
@roles('webserver', 'dbserver')
@parallel
def base():
    run('yum -y install epel-release')


@task
def deploy():
    execute(base)
    execute(webtask)
    execute(dbtask)

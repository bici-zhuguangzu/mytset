#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-07 14:00:43
# @Author  : guangzu (guangzu_zhu@163.com)
# @Link    : blog.zhuguangzu.xyz
# @Version : $Id$

import remoteexec

ips = "192.168.12.203"
url = "192.168.12.209/shell/default.conf"
hostnames = "node02"


def deploys():
    commands = "echo %s" % hostnames + "> hostname.txt&&curl -s %s" % url
    print remoteexec.execOnRemote(ips, commands)


def main():
    deploys()


if __name__ == '__main__':
    main()

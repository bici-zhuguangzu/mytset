#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-15 17:43:33
# @Author  : guangzu (guangzu_zhu@163.com)
# @Link    : blog.zhuguangzu.xyz
# @Version : $Id$

import paramiko


def translate(remote, local):
    t = paramiko.Transport(('192.168.12.210', 22))
    t.connect(username="root", password="123qwe")
    sftp = paramiko.SFTPClient.from_transport(t)
    remote = remote
    local = local
    sftp.put(local, remote)
    return remote


def main():
    remote = "/root/111.py"
    local = "./test.py"
    print translate(remote, local)


if __name__ == '__main__':
    main()

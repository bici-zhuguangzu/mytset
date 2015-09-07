#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-07 10:16:14
# @Author  : guangzu (guangzu_zhu@163.com)
# @Link    : blog.zhuguangzu.xyz
# @Version : $Id$

import paramiko

username = "root"
passwd = "123qwe"


def execOnRemote(host, command):
    global output
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, 22, username, passwd)
    stdin, stdout, stderr = ssh.exec_command(command)
    err = stderr.read()
    output = stdout.read()
    if err != "":
        return err
    else:
        return output
    ssh.close


def main():
    print execOnRemote("192.168.12.203", "ls")

if __name__ == '__main__':
    main()

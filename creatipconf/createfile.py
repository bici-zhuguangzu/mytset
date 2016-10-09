#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-09 10:49:53
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

from jinja2 import Template


fileanme = '111.txt'


def renderfromfile():
    ipdict = {}
    with open(fileanme) as f:
        content = f.readlines()
        f.close
        for ipconf in content:
            iparray = ipconf.strip('\n').split(' ')
            ip = iparray[0]
            bond = iparray[-1]
            ipdict[ip] = bond
            content = renderfile(ip, bond)
            conffile = open("ifcfg-" + bond, "a")
            conffile.write(content)
            conffile.close
    return ipdict


def renderfile(ip, bond):
    with open("temp.jinja") as ff:
        tmpl = Template(ff.read())
    content = tmpl.render(
        ipaddr=ip,
        bondname=bond
    )
    return content


if __name__ == '__main__':
    renderfromfile()
    # renderfile("123.123.123.123", "bond1.23")

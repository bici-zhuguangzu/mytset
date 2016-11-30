#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-30 21:16:19
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from jinja2 import Template


def rendernginxconf(vip, proxyip):
    with open('nginx.tmp') as f:
        tmpl = Template(f.read())
    content = tmpl.render(vip=vip, pip=proxyip)
    print(content)

if __name__ == '__main__':
    rendernginxconf('123.123.123.123', '234.234.234.234')

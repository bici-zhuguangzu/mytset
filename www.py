#!/usr/bin/env python
# -*- coding: utf-8 -*-
<<<<<<< Updated upstream
# @Date    : 2016-10-06 14:56:52
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

"""Qingchat CLI

Usage:
    www search group name <group> <name>
    www search source ip <sourceip>
    www search lanip ip <lanip>
Options:
  -h --help     Show this screen.
  -v --version     Show version.
"""

import os
import time
from docopt import docopt

def function():
    pass


if __name__ == '__main__':
    argumemt = docopt(__doc__, version='wwww 0.0.1')
<<<<<<< HEAD
    print(argumemt['<group>'])
    print(argumemt['<name>'])
=======
    print argumemt['<group>']
    print argumemt['<name>']
=======
# @Date    : 2016-10-06 22:19:36
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

"""

Usage:
    www ip port <ip> <port> [options]
    www ip [options]

Options:
    -h --help   show this screen.
    -o file
    -v --verbose    print status messages
    -t=<kn>

"""

import os
from docopt import docopt

def test(ip):
    print ip


if __name__ == '__main__':
    argument = docopt(__doc__)
    print argument
    ip = argument['<ip>']
    test(ip)
>>>>>>> Stashed changes
>>>>>>> origin/master

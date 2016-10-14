#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
    print(argumemt['<group>'])
    print(argumemt['<name>'])
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-12 03:44:41
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# @Version : $Id$

# test return 2 values


def out(i, k):
    return i + '\n' + k


def main():
    print out("1", "2")


if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-09 11:06:55
# @Author  : guangzu (guangzu_zhu@163.com)
# @Link    : blog.zhuguangzu.xyz
# @Version : $Id$

import json as js

FileName = "../test.json"


def ReadFile():
    f = open(FileName, "r")
    for line in f.readlines():
        return line
    f.close


def ReadJson():
    data = ReadFile()
    JsonDict = js.loads(data)
    return JsonDict


def GainKeys():
    dict = ReadJson()
    for keys in dict.keys():
        return keys


def main():
    print ReadJson()

if __name__ == '__main__':
    main()

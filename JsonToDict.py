#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-09 11:06:55
# @Author  : guangzu (guangzu_zhu@163.com)
# @Link    : blog.zhuguangzu.xyz
# @Version : $Id$

import json

FileName = "../test.json"


def ReadFile():
    f = open(FileName, "r")
    data = f.readline()
    f.close
    return data


def ReadJson():
    data = ReadFile()
    JsonDict = json.loads(data)
    return JsonDict


def GainKeys():
    dict = ReadJson()
    for keys in dict.keys():
        print keys


def main():
    GainKeys()

if __name__ == '__main__':
    main()

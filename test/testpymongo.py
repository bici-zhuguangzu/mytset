#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-10 16:44:49
# @Author  : guangzu (guangzu_zhu@163.com)
# @Link    : blog.zhuguangzu.xyz
# @Version : $Id$

import pymongo


def manual_iter(f):
    try:
        while True:
            line = next(f)
            print line
    except StopIteration:
        pass


def conn():
    conn = pymongo.MongoClient('192.168.12.210', 27017)
    return conn


def coll():
    db = conn().bici
    coll = db.note
    return coll


def query():
    return coll().find()


def out():
    i = query()
    manual_iter(i)


def main():
    print out()


if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-10 17:38:13
# @Author  : guangzu (guangzu_zhu@163.com)
# @Link    : blog.zhuguangzu.xyz
# @Version : $Id$

import pymongo


def conn():
    conn = pymongo.MongoClient()
    return conn


def coll():
    db = conn().bici()
    coll = db.note()
    return coll


def query():
    print coll().find()


def main():
    query()


if __name__ == '__main__':
    main()

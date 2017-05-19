#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-21 16:49:22
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

class testa(object):
    """docstring for testa"""
    def __init__(self, **arg):
        super(testa, self).__init__()
        self.arg = arg


    def test(self):
        for k,v in self.arg.items():
            setattr(self,k,v)



if __name__ == '__main__':
    t = testa(a="b",c="d")
    t.test()
    print(t.c)

        

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-19 15:41:59
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# @Version : $Id$

class testdict(dict):
    """docstring for testdict"""
    def __init__(self):
        super(testdict, self).__init__()

    def printvalues(self):
        _data = [a for a,b in self.items()]
        return _data

if __name__ == '__main__':
    a= testdict()
    a['a']='b'
    a['b'] = 'c'
    print(a.printvalues())
        

        

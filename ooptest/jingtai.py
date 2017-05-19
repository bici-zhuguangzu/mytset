#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-21 08:09:41
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$



class guangzu(object):
    """docstring for guangzu"""
    __sum = 'ok'
    def __init__(self):
        super(guangzu, self).__init__()
        pass

    def setarg(self, arg):
        self.arg = arg


    @classmethod
    def test(cls):
        return 'test'


    @staticmethod
    def testsf():
        # print('1')
        name = 'guangzu'
        return name

    @classmethod
    def testcf(cls):
        return cls.test()


    def __intra(self):
        return 'intra'

    def useintra(self):
        return self.__intra()

class guangzu1(guangzu):
    """docstring for guangzu1"""
    __sum = 'false'
    er = 'false'
    def __init__(self, arg):
        super(guangzu1, self).__init__()
        self.arg = arg
        __sum = 'false'

    @classmethod
    def test(cls):
        return 'test1'

    def testname(self):
        print(self.test())
        return self.qq

    @classmethod
    def testself(cls):
        return cls.__sum

    def useintra(self):
        return self.__intra()



if __name__ == '__main__':
    # print(guangzu.testcf())
    # print(guangzu1.testcf())
    # print(guangzu.testsf())
    t = guangzu()
    t1 = guangzu1('1')
    print(guangzu1.er)
    # print(t.testself())
    print(guangzu1.testsf())
    print(t.useintra())

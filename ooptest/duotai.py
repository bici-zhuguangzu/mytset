#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-21 15:46:55
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

class preson(object):
    """docstring for preson"""
    def __init__(self):
        super(preson, self).__init__()
        self.speed = '10'       
    
    def move(self):
        return self.speed   

class animal(object):
    """docstring for animal"""
    def __init__(self):
        super(animal, self).__init__()
        self.speed = '20'

    def move(self):
        return self.speed

class renma(preson,animal):
    """docstring for renma"""
    speed = 50
    def __init__(self):
        super(renma, self).__init__()


    def setspeed(self):
        self.speed = 40

    @classmethod
    def move(cls):
        return cls.speed

    def printspeed(self):
        print(self.speed)
        
        

if __name__ == '__main__':
    t = preson()
    a = animal()
    h= renma()
    for i in (t,a,h):
        print(i.move())
    h.setspeed()
    h.printspeed()

        

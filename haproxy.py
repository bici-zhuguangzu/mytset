#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-12 16:11:43
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

import json
import os


def ReadFile():
    with open('haproxy', 'rw') as f:
        data = f
    return data.readlines()


def WriteNote(Note):
    f = ReadFile()
    f.write(Note)
    f.close


def Notice():
    print '1、获取ha记录'
    print '2、增加ha记录'
    print '3、删除ha记录'


def GetInput():
    Num = input('请输入操作序号：')
    return Num


def GainNote():
    print "输入要获取的模块 \n For EXAMPLE: \
        www.oldboy.org"
    read = raw_input('请输入backend:')
    backend = "backend " + read + '\n'
    # print backend
    with open('haproxy', 'rw') as f:
        for line in open('haproxy', 'r'):
            line = f.readline()
            if line == backend:
                print line
                continue
                if line is None:
                    break
            else:
                print line



def AddNote():
    print '输入要获取的模块 \n For EXAMPLE: \
    {"backend": "test.oldboy.org", \
    "record": {"server": "100.1.7.9", "weight": 20, "maxconn": 30}}'
    read = raw_input('请输入要新加的记录：')
    with open('haproxy', 'a') as f:
        read_dict = json.loads(read)
        backend_title = read_dict['backend']
        recordStr = read_dict['record']
        # record = json.loads(recordStr)
        print read_dict
        server = recordStr['server'].encode("utf-8")
        weight = recordStr['weight']
        maxconn = recordStr['maxconn']
        # print type(server)
        backend = "backend " + backend_title + '\n'
        record = '\t' + "server " + server + " weight " + \
            str(weight) + " maxconn " + str(maxconn)
        print record
        for line in open('haproxy', 'r'):
            if line == backend:
                f.write('\n'+record)
                break
        else:
            content = '\n' + backend + record + '\n'
            f.write(content)
    f.close


def DelNote():
    print '输入要获取的模块 \n For EXAMPLE: \
    {"backend": "test.oldboy.org", \
    "record": {"server": "100.1.7.9", "weight": 20, "maxconn": 30}}'
    with open('haproxy', 'rw') as f:
        read = raw_input('请输入要删除的记录：')
        read_dict = json.loads(read)
        backend_title = read_dict['backend']
        recordStr = read_dict['record']
        # record = json.loads(recordStr)
        print read_dict
        server = recordStr['server'].encode("utf-8")
        weight = recordStr['weight']
        maxconn = recordStr['maxconn']
        # print type(server)
        backend = "backend " + backend_title + '\n'
        record = '\t' + "server " + server + " weight " + \
            str(weight) + " maxconn " + str(maxconn)
        print record
        for line in open('haproxy', 'r'):
            line = f.readline()
            if line == backend:
                with open('haproxybak', 'a') as bak:
                    bak.write(line)
                if line == record:
                    pass
            else:
                with open('haproxybak', 'a') as bak:
                    bak.write(line)



if __name__ == '__main__':
    while True:
        Notice()
        Num = GetInput()
        if Num == 1:
            GainNote()
        elif Num == 2:
            AddNote()
        elif Num == 3:
            DelNote()
        else:
            print '请输入正确的编号'

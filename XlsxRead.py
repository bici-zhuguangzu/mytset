#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
import xlrd

FileName= "/root/2.xlsx"


def ReadXls():
    global HostName
    global HostIP
    data= xlrd.open_workbook(FileName)
    table= data.sheets()[0]
    HostName=table.col_values(1)
    HostIP=table.col_values(7)


def MakeDict():
    nvs = zip(HostName,HostIP)
    HostDict = dict( (name,value) for name,value in nvs)
    print type(HostDict)


def main():
    ReadXls()
    MakeDict()


if __name__ == '__main__':
        main() 
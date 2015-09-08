#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlrd

FileName = "/Users/zhuguangzu1/Documents/2.xlsx"


def ReadXls(filename):
    data = xlrd.open_workbook(filename)
    table = data.sheets()[0]
    return table


def MakeDict(filename):
    XlsxData = ReadXls(filename)
    HostName = XlsxData.col_values(1)
    HostIP = XlsxData.col_values(7)
    nvs = zip(HostName, HostIP)
    HostDict = dict((name, value) for name, value in nvs)
    del HostDict[u'名称']
    del HostDict[u'ResourceCenter']
    return HostDict


def CountOfDict():
    HostDict = MakeDict(FileName)
    count = 0
    for key in HostDict.keys():
        count = count + 1
    return count


def MakeDictFormXls():
    print MakeDict(FileName)


def main():
    MakeDictFormXls()
    print CountOfDict()

if __name__ == '__main__':
    main()

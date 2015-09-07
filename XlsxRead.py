#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlrd

FileName = "/Users/zhuguangzu1/Documents/2.xlsx"


def ReadXls():
    data = xlrd.open_workbook(FileName)
    table = data.sheets()[0]
    return table


def MakeDict():
    XlsxData = ReadXls()
    HostName = XlsxData.col_values(1)
    HostIP = XlsxData.col_values(7)
    nvs = zip(HostName, HostIP)
    HostDict = dict((name, value) for name, value in nvs)
    return HostDict


def MakeDictFormXls():
    ReadXls()
    print MakeDict()


def main():
    MakeDictFormXls()

if __name__ == '__main__':
    main()

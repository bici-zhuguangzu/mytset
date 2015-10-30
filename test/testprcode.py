#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-12 02:57:30
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# @Version : $Id$

import qrcode


def input():
    global content2
    content1 = raw_input("inut 公司:")
    content2 = raw_input("inut 编号:")
    return "公司:" + content1 + '\n' + "编号：" \
        + content2


def createimg():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(input())
    qr.make(fit=True)
    img = qr.make_image()
    img.save(content2 + '.png')


def main():
    createimg()


if __name__ == '__main__':
    main()

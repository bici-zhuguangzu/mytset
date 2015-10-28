#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-27 20:13:06
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/test')
def deploys():
    print '1111'
    a = '3'
    return 'this is %s' % a


@app.route('/temp')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='192.168.10.122', port=3000)

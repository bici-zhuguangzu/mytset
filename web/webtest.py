#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-22 10:01:19
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# @Version : $Id$

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>hello world!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>hello , %s!</h1>' % name


if __name__ == '__main__':
    app.run(debug=True)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-22 10:25:18
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# @Version : $Id$

from flask import request
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s </p>' % user_agent

if __name__ == '__main__':
    app.run(debug=True)
